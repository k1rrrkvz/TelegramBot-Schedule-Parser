import os
import requests
import datetime

import openpyxl

from selenium import webdriver
from selenium.webdriver.common.by import By



class WebScraperFileDownloader:

    def get_links(self):

        driver = webdriver.Chrome()
        driver.get("https://spo-13.mskobr.ru/uchashimsya/raspisanie-kanikuly")
        links = driver.find_elements(By.XPATH, "//p/a[contains(@href, '.xlsx')]")

        links_set = []
        for link in links:
            href = link.get_attribute("href")
            links_set.append(href)

        driver.quit()

        result = [(link) for link in links_set]
        #return result


    def download_files(self, url, file_count, name):

        folder_path = f"src\\chrome_driver\\data\\{name}"

        response = requests.get(url)

        if response.status_code == 200:

            for count in range(1, file_count+1):

                file_name = f"file{count}_course_{name}.xlsx"
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"Файл успешно скачан. Время: {datetime.datetime.now().time()} Код сервера: {response.status_code}")
        else:
            print(f"Ошибка при скачивании файла: {url} \nВремя: {datetime.datetime.now().time()} Код сервера: {response.status_code}")

# Работу этого класса временно заменяет файл crawler.parserXL.py 
class ExcelParser:

    def parse_cells(self, path, sheet):

        wb = openpyxl.load_workbook(path)
        sheet = wb[sheet]
        
        # Матрица с диапазонами ячеек
        ranges = [
            (4, 11),
            (12, 19),
            (20, 27),
            (28, 35),      
            (36, 43)
        ]    

        # Общее расписание из всех чанков
        timetable = []

                                                                                # работа с конкретной группой 
        for column in range(3, 12, 2):
                                                                                # проход по всем диапазонам ячеек
            for rangeStart, rangeEnd in ranges:
                                                                                # отдельный список (чанк) для каждого дня
                chunk = []
                                                                                # работа с конкретным диапазоном
                for index in range(rangeStart, rangeEnd + 1):
                                                                                # Получаем значения из ячеек 
                    cellValue = sheet.cell(row=index, column=column).value
                    chunk.append(cellValue)
                                                                                # Добавляем каждый список (чанк) в общий список    
                timetable.append(chunk)

        #return timetable

