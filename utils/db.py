import psycopg2

import db_config


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
    return cursor
