from dataclasses import dataclass


@dataclass
class DatabaseCredentials:
    host: str
    port: int
    user: str
    password: str
    dbname: str

# Тоже самое что и датакласс
# class DatabaseCreds:
#     def __init__(self, host, port, user, password, dbname):
#         self.host = host
#         self.port = port
#         self.user = user
#         self.password = password 
#         self.dbname = dbname

@dataclass
class CurlParameters:
    method: str
    url: str
    flag: str


# curl -X POST url 