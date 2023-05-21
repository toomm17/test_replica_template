import json
import pathlib


def get_json_data():
    """
        Фикстура для получения имен потоков из json конфига
    """
    json_config_path = pathlib.Path('config.json')

    with open(json_config_path) as file:
        data = json.load(file)
        return data