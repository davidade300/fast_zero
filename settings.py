import os

from dotenv import load_dotenv

# from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(
#         env_file='.env',
#         env_file_encoding='utf-8',
#     )
#     DATABASE_URL: str
