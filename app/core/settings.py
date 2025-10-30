from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

@lru_cache(maxsize=1)
def get_settings():
    return Settings()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file='.env',
        env_file_encoding='utf-8')

    deepl_api_key: str = ""
