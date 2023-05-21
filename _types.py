from dataclasses import dataclass


@dataclass
class DatabaseCredentials:
    host: str
    port: int
    user: str
    password: str
    dbname: str


@dataclass
class CurlParameters:
    """
        Параметры curl для запуска потока
    """
    method: str
    url: str
    flag: str


