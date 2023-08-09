from aiogram import executor
from handlers import dp

if __name__ == "__main__":
    print("Бот запущен!")
    executor.start_polling(dp, skip_updates = True)     # все ранее отправленные сообщения боту, когда он был выключен, будут пропущены
