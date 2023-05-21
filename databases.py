from sqlalchemy import create_engine

import config


if __name__ == '__main__':
    engine = create_engine(
        f'postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}'
    )

    print(engine)
