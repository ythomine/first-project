set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

setup:
    uv sync --locked

check:
    uv run --locked ruff check .
    uv run --locked ruff format --check .
    SECRET_KEY=test-only-key-do-not-deploy-test-only-key-do-not-deploy ALLOWED_HOSTS='["localhost"]' DJANGO_SETTINGS_MODULE=tests.settings uv run --locked mypy
    uv run --locked lint-imports
    SECRET_KEY=test-only-key-do-not-deploy-test-only-key-do-not-deploy ALLOWED_HOSTS='["localhost"]' uv run --locked python manage.py check --settings=tests.settings
    just test

test *args:
    uv run --locked pytest {{args}}

smoke:
    uv run --locked pytest tests/smoke

run:
    uv run --locked python manage.py runserver

db-up:
    docker compose up -d --wait

db-down:
    docker compose stop
