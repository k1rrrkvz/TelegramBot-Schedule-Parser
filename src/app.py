import asyncio
import sched, time
from aiogram import executor
from handlers import dp
from chrome_driver.main import runParser 

"""def def_runParser():
    while True:
        os.system('python путь_к_файлу.py')
        print("Парсер запущен")"""


if __name__ == "__main__":
    #asyncio
    print("Бот запущен!")
    executor.start_polling(dp, skip_updates = True)     # все ранее отправленные сообщения боту, когда он был выключен, будут пропущены
    


