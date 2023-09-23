import os
import re
import requests
import datetime
import openpyxl

from bs4 import BeautifulSoup



class WebScraperFileDownloader:

    def get_links(self):

        link = 'https://spo-13.mskobr.ru/uchashimsya/raspisanie-kanikuly'
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for a in soup.find_all('a', href=True):
            url = a['href']
            parts = re.split(r'/', url)
            if 'files' in parts and 'attach_files' in parts:
                links.append(url)

        i = len(links) - 1
        url = f"https://spo-13.mskobr.ru/{links[i]}"
        return url


    def download_file(self, url, name):

        folder_path = f"src\\chrome_driver\\data\\{name}"

        response = requests.get(url)

        if response.status_code == 200:
            file_name = f"{name}.xlsx"
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"File downloaded successfully. Time: {datetime.datetime.now().time()} Status Code: {response.status_code}")
        else:
            print(f"Error downloading file: {url}\nTime: {datetime.datetime.now().time()} Status Code: {response.status_code}")

class ExcelDataParser():

    def readDataShankursky(self, path, sheet):
        
        wb = openpyxl.load_workbook(path)
        sheet = wb[sheet]
        
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

        return timetable

