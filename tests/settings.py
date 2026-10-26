"""Configuration déterministe pour les outils et tests, sans credentials distants."""

import os

# Valeurs de test publiques ; aucune clé de déploiement n'est requise par les outils.
os.environ.setdefault("SECRET_KEY", "test-only-key-do-not-deploy-" * 3)
os.environ.setdefault("ALLOWED_HOSTS", '["testserver", "localhost", "127.0.0.1"]')

from revenue_app.config.settings import *  # noqa: E402, F403

DEBUG = False
ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
