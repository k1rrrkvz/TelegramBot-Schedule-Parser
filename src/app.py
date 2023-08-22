import handlers
from aiogram import executor
from loader import dp


if __name__ == "__main__":
    print("Bot running!")
    executor.start_polling(dp, skip_updates = True)     # все ранее отправленные сообщения боту, когда он был выключен, будут пропущены
    