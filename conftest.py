import pytest
import psycopg2

import db_config
import utils


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
def repl_thr_list():
    """
        Получаем из config.json все потоки
        :return: list[string]
    """
    json_data = utils.get_json_data()
    return json_data['threads']['list']


@pytest.fixture()
def multistart_repl_thr():
    """
        Получаем из config.json все потоки для многопоточного запуска
        :return: list[string]
    """
    json_data = utils.get_json_data()
    threads_list = [
        thread for thread in json_data['threads']['list'] 
        if thread['is_single_run'] is False
    ]
    return threads_list


@pytest.fixture()
def singlestart_repl_thr():
    """
        Получаем из config.json все потоки для однопоточного запуска
        :return: list[string]
    """
    json_data = utils.get_json_data()
    threads_list = [
        thread for thread in json_data['threads']['list'] 
        if thread['is_single_run'] is True
    ]
    return threads_list
