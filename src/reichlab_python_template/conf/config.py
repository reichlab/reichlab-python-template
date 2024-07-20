"""Class to pull configuration settings from environment variables."""

from typing import Tuple, Type

from pydantic.types import SecretStr
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)
from reichlab_python_template import CONFIG_PATH


class AppConfig(BaseSettings):
    """Define app configuration settings."""

    model_config = SettingsConfigDict(toml_file=CONFIG_PATH)

    ### Define the application's configuration fields here.
    # Values provided here will be overridden by values in the
    # following places (in order of precedence):
    # 1. Environment variables
    # 2. config.py
    default_greeting: str = "G'day!"
    starfleet_api_url: str
    starfleet_api_token: SecretStr

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[
        PydanticBaseSettingsSource,
        PydanticBaseSettingsSource,
        TomlConfigSettingsSource,
        PydanticBaseSettingsSource,
        PydanticBaseSettingsSource,
    ]:
        """Customize the order of precendece for finding settings."""
        return (
            env_settings,
            dotenv_settings,
            TomlConfigSettingsSource(settings_cls),
            init_settings,
            file_secret_settings,
        )


def get_config() -> AppConfig:
    """Return the application config values."""
    return AppConfig()
