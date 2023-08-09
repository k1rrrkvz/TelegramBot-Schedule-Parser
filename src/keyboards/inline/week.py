from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def defDays():

    choiceDayKB = InlineKeyboardMarkup(row_width=2)

    buttonMonday = InlineKeyboardButton(text="Понедельник", callback_data="bMonday")
    buttonTuesday = InlineKeyboardButton(text="Вторник", callback_data="bTuesday")
    buttonWednesday = InlineKeyboardButton(text="Среда", callback_data="bWednesday")
    buttonThursday = InlineKeyboardButton(text="Четверг", callback_data="bThursday")
    buttonFriday = InlineKeyboardButton(text="Пятница", callback_data="bFriday")
    buttonWeek = InlineKeyboardButton(text="Неделя", callback_data="bWeek")

    choiceDayKB.insert(buttonMonday)
    choiceDayKB.insert(buttonTuesday)
    choiceDayKB.insert(buttonWednesday)
    choiceDayKB.insert(buttonThursday)
    choiceDayKB.insert(buttonFriday)
    choiceDayKB.insert(buttonWeek)

    return choiceDayKB