"""
    Файл для получения переменных окружения
"""
import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB_NAME = os.environ['POSTGRES_DB_NAME']
