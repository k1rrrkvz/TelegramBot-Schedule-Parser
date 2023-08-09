from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def addInlieButton(name):

    addButtonKB = InlineKeyboardMarkup(row_width=1)

    buttonCreater = InlineKeyboardButton(text=f"{name}", callback_data="b" + f"{name}")

    addButtonKB.insert(buttonCreater)

    return(addButtonKB)