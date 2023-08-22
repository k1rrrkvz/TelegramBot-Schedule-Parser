<<<<<<< HEAD
import handlers
from aiogram import executor
from loader import dp


if __name__ == "__main__":
    print("Bot running!")
    executor.start_polling(dp, skip_updates = True)     # все ранее отправленные сообщения боту, когда он был выключен, будут пропущены
    
=======
from aiogram import executor
from handlers import dp

if __name__ == "__main__":
    print("Бот запущен!")
    executor.start_polling(dp, skip_updates = True)     # все ранее отправленные сообщения боту, когда он был выключен, будут пропущены
>>>>>>> cb6c3055f791e682d726ce34f3c48bd0da4fe414
