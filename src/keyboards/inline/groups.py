from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def defaultGroups():

    choiceGroupKB = InlineKeyboardMarkup(row_width=2)

    buttonGroup0 = InlineKeyboardButton(text="11O", callback_data="b0")
    buttonGroup1 = InlineKeyboardButton(text="32ИС", callback_data="b1")
    buttonGroup2 = InlineKeyboardButton(text="32ИСд", callback_data="b2")
    buttonGroup3 = InlineKeyboardButton(text="2ИС", callback_data="b3")
    buttonGroup4 = InlineKeyboardButton(text="1ИС", callback_data="b4")

    choiceGroupKB.insert(buttonGroup0)
    choiceGroupKB.insert(buttonGroup1)
    choiceGroupKB.insert(buttonGroup2)
    choiceGroupKB.insert(buttonGroup3)
    choiceGroupKB.insert(buttonGroup4)

    return choiceGroupKB

