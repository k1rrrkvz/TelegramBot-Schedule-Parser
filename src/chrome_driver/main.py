from linkScraper import linkCatcher
from download import downloadFile


def runParser():
    result = linkCatcher()  # Вызов функции и получение результата

    # Распределяем ссылки по корпусам
    bibirevo = result[0:4]
    yaroslavsky = result[4:8]
    shankursky = result[8]

    # Проходимся по ссылкам в списке
    # Параметр i указывает на кол-во файлов в списках bibirevo, yaroslavsky, shankursky
    for link in bibirevo:
        downloadFile(url = link, i = len(bibirevo), name = "Bibirevo")

    for link in yaroslavsky:
        downloadFile(url = link, i = len(yaroslavsky), name = "Yaroslavsky")

    downloadFile(url = shankursky, i = 1, name = "Shankursky")

    return(result)


#runParser()
