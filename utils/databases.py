import psycopg2
import sshtunnel

import config
import _types


def create_ssh_connection(credentials: _types.DatabaseCredentials):
    """
        Создаем коннект по ssh для удаленного подключения к базе данных
    """
    server = sshtunnel.SSHTunnelForwarder(
        (credentials.host, credentials.port),
        ssh_username=credentials.user,
        ssh_password=credentials.password,
        remote_bind_address=('localhost', credentials.port),
        local_bind_address=('localhost', credentials.port)
    )
    server.start()
    return server


def create_postgres_connection(credentials: _types.DatabaseCredentials) -> psycopg2.connect:
    """
        Создаем подключение к пострегс (пока что локально)
    """
    try:
        connection = psycopg2.connect(
            dbname=credentials.dbname,
            host=credentials.host,
            port=credentials.port,
            user=credentials.user,
            password=credentials.password
        )

    except psycopg2.OperationalError:
        raise Exception('Could not connect to db')    
    
    return connection


def create_oracle_connection(credentials: _types.DatabaseCredentials):
    pass


def create_mysql_connection(credentials: _types.DatabaseCredentials):
    pass


def test_function():
    pass


if __name__ == '__main__':
    postgres_credentials = _types.DatabaseCredentials(
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        dbname=config.POSTGRES_DB_NAME
    )

    postgres_connection = create_postgres_connection(postgres_credentials)

    # cursor = postgres_connection.cursor()
    # cursor.execute('asdasdsad')
    # postgres_connection.commit()
    # postgres_connection.close()

    with postgres_connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Shemet (id, num, data) VALUES (1, 2, 'dadadadad')"
        )
        
        postgres_connection.commit()
    