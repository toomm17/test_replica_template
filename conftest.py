import os

import pytest
import psycopg2

import db_config
import utils


json_data = utils.get_json_data()
thrs_list = json_data['threads']['list']


@pytest.fixture()
def postgres_cursor():
    """
        Фикстура для получения коннекта к постгресу
        После завершения теста коннект закрывается
    """
    conn = psycopg2.connect(
        dbname=db_config.POSTGRES_DB_NAME,
        user=db_config.POSTGRES_USER,
        password=db_config.POSTGRES_PASSWORD,
        host=db_config.POSTGRES_HOST,
        port=db_config.POSTGRES_PORT
    )
    cursor = conn.cursor()
    yield cursor
    cursor.close()
    conn.close()


@pytest.fixture()
def config():
    json_data = utils.get_json_data(os.path.abspath('config.json'))
    return json_data['threads']
