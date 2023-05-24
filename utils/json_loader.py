import json
import pathlib


def get_json_data():
    """
        Функция для получения данных в config.json
    """
    json_config_path = pathlib.Path('config.json')

    with open(json_config_path) as file:
        data = json.load(file)
        return data