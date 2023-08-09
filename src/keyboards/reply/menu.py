from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def defUpgrade():

    upgradeKB = ReplyKeyboardMarkup(resize_keyboard=True)
    buttonDataUpd = KeyboardButton(text="Обновить данные")

    upgradeKB.add(buttonDataUpd)

    return upgradeKB