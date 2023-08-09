from selenium import webdriver
from selenium.webdriver.common.by import By
    
    # Этот файл для скраппинга ссылок со страницы колледжа

def linkCatcher():

    # Инициализация драйвера Selenium
    driver = webdriver.Chrome()

    # Открытие страницы
    driver.get("https://spo-13.mskobr.ru/uchashimsya/raspisanie-kanikuly")

    # Нахождение всех ссылок на странице.
    # В выражении //p/a[contains(@href, '.xlsx')] используется XPath для поиска элементов <a> (ссылки), 
    # содержащих атрибут href, в котором присутствует подстрока ".xlsx".
    
    # // - два слэша указывают на то, что поиск элемента будет осуществляться от корневого узла документа.
    # p - выбирает все элементы <p>.
    # /a - выбирает дочерние элементы <a> относительно элементов <p>.
    # [contains(@href, '.xlsx')] - это условие, которое фильтрует только те элементы <a>, у которых атрибут 
    # href содержит подстроку ".xlsx". contains - функция XPath, которая проверяет, содержит ли строка 
    # (значение атрибута href) указанную подстроку (".xlsx").

    # Таким образом, данное XPath-выражение будет находить все ссылки <a>, у которых атрибут href содержит 
    # подстроку ".xlsx" и которые находятся внутри элементов <p>.
    links = driver.find_elements(By.XPATH, "//p/a[contains(@href, '.xlsx')]")

    links_set = []
    # Итерация по найденным ссылкам
    for link in links:
        href = link.get_attribute("href")
        links_set.append(href)

    # Закрытие браузера
    driver.quit()

    # result = [(numbering, link) for numbering, link in enumerate(links_set, start=1)] # нумерация ссылок
    result = [(link) for link in links_set]
    return result

    
