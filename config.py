import os

from dotenv import load_dotenv


env = load_dotenv()

if not env:
    raise Exception('Cannot load postgres credentials')

POSTGRES_PORT = int(os.environ['POSTGRES_PORT'])
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB_NAME = os.environ['POSTGRES_DB_NAME']
