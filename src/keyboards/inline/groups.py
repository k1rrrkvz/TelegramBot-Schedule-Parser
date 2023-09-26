from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def defaultGroups():

    choiceGroupKB = InlineKeyboardMarkup(row_width=2)

    buttonGroup0 = InlineKeyboardButton(text="11O", callback_data="b0")
    buttonGroup1 = InlineKeyboardButton(text="21О", callback_data="b1")
    buttonGroup2 = InlineKeyboardButton(text="31ИС", callback_data="b2")
    buttonGroup3 = InlineKeyboardButton(text="32ИСд", callback_data="b3")
    buttonGroup4 = InlineKeyboardButton(text="41ИС", callback_data="b4")
    buttonGroup5 = InlineKeyboardButton(text="42ИСд", callback_data="b5")
    buttonGroup6 = InlineKeyboardButton(text="1ИС", callback_data="b6")
    buttonGroup7 = InlineKeyboardButton(text="2ИС", callback_data="b7")
    buttonGroup8 = InlineKeyboardButton(text="3ИС", callback_data="b8")

    choiceGroupKB.insert(buttonGroup0)
    choiceGroupKB.insert(buttonGroup1)
    choiceGroupKB.insert(buttonGroup2)
    choiceGroupKB.insert(buttonGroup3)
    choiceGroupKB.insert(buttonGroup4)
    choiceGroupKB.insert(buttonGroup5)
    choiceGroupKB.insert(buttonGroup6)
    choiceGroupKB.insert(buttonGroup7)
    choiceGroupKB.insert(buttonGroup8)

    return choiceGroupKB

