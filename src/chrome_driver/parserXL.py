#import time
import openpyxl

#start = time.time()

def readDataShankursky(path, sheet):
    
    wb = openpyxl.load_workbook(path)   # Загрузка файла XLSX
    sheet = wb[sheet]                   # Выбор нужного листа
    
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

    return timetable

# Шенкурский
pathToFileShankursky = 'src\\chrome_driver\\data\\Shankursky\\file1_course_Shankursky.xlsx'
sheet = 'Лист1'
dataShankursky = readDataShankursky(pathToFileShankursky, sheet)
print(dataShankursky)

#end = time.time() - start 
#print(f"time: {end}") 
