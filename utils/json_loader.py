import json


def get_json_data(json_path: str):
    """
        Функция для получения данных в config.json
    """
    with open(json_path) as file:
        data = json.load(file)
        return data
