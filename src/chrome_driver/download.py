import os
import requests
import datetime

# Параметр i указывает на кол-во файлов
def downloadFile(url, i, name):

    folder_path = f"src\\chrome_driver\\data\\{name}"  # Папка, в которую сохранить файл

    response = requests.get(url)                  # Получаем ответ от GET-запроса

    if response.status_code == 200:

        for count in range(1, i+1):

            # Путь и формат сохранения файлов
            file_name = f"file{count}_course_{name}.xlsx"
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Файл успешно скачан. Время: {datetime.datetime.now().time()} Код сервера: {response.status_code}")
    else:
        print(f"Ошибка при скачивании файла: {url} \nВремя: {datetime.datetime.now().time()} Код сервера: {response.status_code}")

