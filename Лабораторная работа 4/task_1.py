# TODO решите задачу

import json


def task() -> float:
    with open('D:\Python\Course Python английский\Работа с источниками данных\Лабораторная работа\Найти сумму произведений из списка словарей\input.json', 'r') as file:
        data = json.load(file)

    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)


print(task())

