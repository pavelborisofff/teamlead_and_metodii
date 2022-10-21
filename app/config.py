from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Telegram
    BOT_TOKEN: Optional[str] = None
    DEV_BOT_TOKEN: str

    # Dev
    DEV: bool = False
    LONG_POLLING: bool = False
    LOGGING_LEVEL: str = 'INFO'

    class Config:
        env_file = './.env'


settings = Settings()
