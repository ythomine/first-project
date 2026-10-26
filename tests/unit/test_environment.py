import pytest
from django.core.exceptions import ImproperlyConfigured
from pydantic import ValidationError

from revenue_app.config.environment import Environment, load_environment


def test_valid_configuration_has_typed_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("DB_PORT", "5433")
    settings = Environment(_env_file=None)
    assert settings.db_port == 5433
    assert settings.debug is False


def test_production_requires_hosts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("ALLOWED_HOSTS", "[]")
    with pytest.raises(ValidationError, match="ALLOWED_HOSTS"):
        Environment(_env_file=None)


def test_invalid_secret_is_not_exposed(monkeypatch: pytest.MonkeyPatch) -> None:
    value = "short-sensitive-value"
    monkeypatch.setenv("SECRET_KEY", value)
    with pytest.raises(ImproperlyConfigured) as error:
        load_environment()
    assert value not in str(error.value)


def test_missing_secret_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECRET_KEY")
    with pytest.raises(ValidationError, match="secret_key"):
        Environment(_env_file=None)


def test_malformed_list_has_a_safe_error(monkeypatch: pytest.MonkeyPatch) -> None:
    value = "malformed-sensitive-input"
    monkeypatch.setenv("ALLOWED_HOSTS", value)
    with pytest.raises(ImproperlyConfigured) as error:
        load_environment()
    assert value not in str(error.value)
