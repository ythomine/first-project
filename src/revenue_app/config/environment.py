from pydantic import Field, SecretStr, ValidationError, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict, SettingsError


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", hide_input_in_errors=True)

    debug: bool = False
    secret_key: SecretStr = Field(min_length=50)
    allowed_hosts: list[str] = []
    csrf_trusted_origins: list[str] = []
    db_host: str = "127.0.0.1"
    db_port: int = Field(default=5432, ge=1, le=65535)
    db_name: str = "revenue_app"
    db_user: str = "revenue_app"
    db_password: SecretStr = SecretStr("")

    @model_validator(mode="after")
    def require_production_hosts(self) -> "Environment":
        if not self.debug and not self.allowed_hosts:
            raise ValueError("ALLOWED_HOSTS est obligatoire lorsque DEBUG=false")
        return self


def load_environment() -> Environment:
    from django.core.exceptions import ImproperlyConfigured

    try:
        return Environment()
    except (ValidationError, SettingsError):
        # Les détails de validation peuvent contenir des entrées secrètes.
        raise ImproperlyConfigured(
            "Configuration invalide. Vérifier les variables documentées dans .env.example."
        ) from None
