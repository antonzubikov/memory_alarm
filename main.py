import psutil
import requests
import time

api_url = 'https://example.com/api/alarm'  # пример URL API для отправки сообщения

memory_threshold = 80  # пороговое значение для потребляемой памяти в процентах (max 80%)

while True:
    memory_usage = psutil.virtual_memory().percent

    if memory_usage > memory_threshold:
        response = requests.post(api_url)
        if response.status_code == 200:
            print('Alarm message send.')
        else:
            print('Alarm message send error.')

    time.sleep(60)
