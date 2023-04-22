import pytest

import _types
import config
import utils


@pytest.fixture()
def postgres():
    postgres_credentials = _types.DatabaseCredentials(
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        dbname=config.POSTGRES_DB_NAME
    )

    postgres_connection = utils.create_postgres_connection(postgres_credentials)
    yield postgres_connection
    postgres_connection.close()


@pytest.fixture()
def test_for_igor():
    print('SETUP TEST FOR IGOR')
    yield 1
    print('TEARDOWN TEST FOR IGOR')

