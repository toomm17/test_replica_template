import pytest

import _types
import utils


# @pytest.fixture()
# def postgres():
#     """
#         Фикстура для получения коннекта к постгресу
#         После завершения теста коннект закрывается
#     """
#     postgres_credentials = _types.DatabaseCredentials(
#         host=config.POSTGRES_HOST,
#         port=config.POSTGRES_PORT,
#         user=config.POSTGRES_USER,
#         password=config.POSTGRES_PASSWORD,
#         dbname=config.POSTGRES_DB_NAME
#     )

#     postgres_connection = utils.create_postgres_connection(postgres_credentials)
#     yield postgres_connection
#     postgres_connection.close()


@pytest.fixture()
def repl_thr_list():
    """
        Получаем из config.json все имена потоков
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
    threads_list = json_data['threads']['list']
    num_threads = json_data['threads']['maxRunning']
    return threads_list[0:num_threads]


@pytest.fixture()
def singlestart_repl_thr():
    """
        Получаем из config.json все потоки для многопоточного запуска
        :return: list[string]
    """
    json_data = utils.get_json_data()
    threads_list = json_data['threads']['list']
    num_threads = json_data['threads']['maxRunning']
    return threads_list[num_threads:]
