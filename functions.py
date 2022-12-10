import csv
import json
from typing import Dict, Union, Optional
from ads.models import Category, Advertisement


"""
Для использования функции convert_from_csv_to_json выполнить в терминале:
1. python manage.py shell
2. from functions import convert_from_csv_to_json
3. convert_from_csv_to_json("data/categories.csv", "data/categories.json")
4. convert_from_csv_to_json("data/ads.csv", "data/ads.json")
"""


def convert_from_csv_to_json(csv_file_name: str, json_file_name: str) -> Optional[str]:
    """
    Преобразует файл формата CSV в файл формата JSON
    :param csv_file_name: Имя файла формата CSV
    :param json_file_name: Имя файла формата JSON
    :return: Опционально сообщение об ошибке
    """
    raw_data: Dict[int, Dict[str, Union[int, str]]] = {}

    try:
        file = open(csv_file_name, encoding="utf-8")
    except FileNotFoundError:
        return f"Файл {csv_file_name} не найден"
    else:
        csv_file_data = csv.DictReader(file)
        for row in csv_file_data:
            try:
                key: int = row["id"]
            except KeyError:
                return "Ключ id не найден"
            else:
                raw_data[key]: Dict[str, Union[int, str]] = row
    finally:
        file.close()

    with open(json_file_name, "w", encoding="utf-8") as file:
        json_data: str = json.dumps(raw_data, indent=4, ensure_ascii=False)
        file.write(json_data)

    return None


"""
Для использования функций create_categories, create_advertisements выполнить в терминале:
1. python manage.py shell
2. from functions import create_categories, create_advertisements
3. create_categories("data/categories.json")
4. create_advertisements("data/ads.json")
"""

"""
Для очистки таблиц выполнить в терминале: python manage.py flush
"""


def create_categories(json_file_name) -> Optional[str]:
    """
    Заполняет таблицу Category данными из файла формата JSON
    :param json_file_name: Имя файла формата JSON
    :return: Опционально сообщение об ошибке
    """
    try:
        file = open(json_file_name, encoding="utf-8")
    except FileNotFoundError:
        return f"Файл {json_file_name} не найден"
    else:
        json_file_data = json.load(file)
        for value in json_file_data.values():
            category = Category(
                name=value["name"]
            )
            category.save()
    finally:
        file.close()
        return None


def create_advertisements(json_file_name) -> Optional[str]:
    """
    Заполняет таблицу Advertisement данными из файла формата JSON
    :param json_file_name: Имя файла формата JSON
    :return: Опционально сообщение об ошибке
    """
    try:
        file = open(json_file_name, encoding="utf-8")
    except FileNotFoundError:
        return f"Файл {json_file_name} не найден"
    else:
        json_file_data = json.load(file)
        for value in json_file_data.values():
            advertisement = Advertisement(
                name=value["name"],
                author=value["author"],
                price=value["price"],
                description=value["description"],
                address=value["address"],
                is_published=value["is_published"].capitalize()
            )
            advertisement.save()
    finally:
        file.close()
        return None
