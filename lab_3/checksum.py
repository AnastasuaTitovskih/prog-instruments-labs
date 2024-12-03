import re
import json
import hashlib
import csv
from typing import List

INPUT_PATH = "lab_3/24.csv"
OUTPUT_PATH = "lab_3/result.json"
REGEX_PATTERNS = {
    "telephone": r"^\+7\-\(\d{3}\)\-\d{3}\-\d{2}\-\d{2}$",
    "height": r"^[1-2]\.\d{2}$",
    "inn": r"^\d{12}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "occupation": r"[А-Я]+|[A-Z]+",
    "latitude": r"^-?[1][1-8][1-9]\.\d+|^-?\d{1,2}\.\d+$",
    "blood_type": r"^(A|B|AB|O)[\u2212+]$",
    "issn": r"^\d{4}-\d{4}$",
    "uuid": r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
    "date": r"^(?:19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
}

def calculate_checksum(indices: List[int]) -> str:
    """
    Вычисляет хеш от списка индексов.

    ВНИМАНИЕ, ВАЖНО! Чтобы сумма получилась корректной, считать, что первая строка с данными csv-файла имеет номер 0
    Другими словами: В исходном csv 1я строка - заголовки столбцов, 2я и остальные - данные.
    Соответственно, считаем что у 2 строки файла номер 0, у 3й - номер 1 и так далее.

    Надеюсь, я расписал это максимально подробно.
    Хотя что-то мне подсказывает, что обязательно найдется человек, у которого с этим возникнут проблемы.
    Которому я отвечу, что все написано в докстринге 

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    indices.sort()
    return hashlib.md5(json.dumps(indices).encode('utf-8')).hexdigest()

def serialize_result(variant_id: int, check_hash: str) -> None:
    """
    Метод для сериализации результатов лабораторной пишите сами.
    Вам нужно заполнить данными - номером варианта и контрольной суммой - файл, лежащий в папке с лабораторной.
    Файл называется, очевидно, result.json.

    ВНИМАНИЕ, ВАЖНО! На json натравлен github action, который проверяет корректность выполнения лабораторной.
    Так что не перемещайте, не переименовывайте и не изменяйте его структуру, если планируете успешно сдать лабу.

    :param variant: номер вашего варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    """
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as file:
        result_content = {
            "variant": variant_id,
            "hash": check_hash
        }
        file.write(json.dumps(result_content, indent=4))

def load_csv_data(file_path: str) -> list:
    """
    Загружает данные из CSV-файла.
    """
    with open(file_path, 'r', encoding='utf-16') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        return [line for line in reader]

if __name__ == "__main__":
    loaded_data = load_csv_data(INPUT_PATH)
    invalid_indices = get_invalid_rows(loaded_data, REGEX_PATTERNS)
    checksum_result = calculate_checksum(invalid_indices)
    serialize_result(24, checksum_result)




