from aiogram import types
from loader import dp, bot

from keyboards.reply import menu
from keyboards.inline import groups

from crawler.main import WebScraperFileDownloader, ExcelParser
from crawler.parserXL import readDataShankursky


scraper = WebScraperFileDownloader()
parser = ExcelParser()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Добро пожаловать!', reply_markup=menu.defUpgrade())
    await message.answer('Выберите группу:', reply_markup=groups.defaultGroups())
    scraper.get_links()
    scraper.download_files()

@dp.message_handler()
async def call_menu(message: types.Message):
    if 'Показать меню' in message.text:
        await message.answer('Выберите группу:', reply_markup=groups.defaultGroups())


@dp.callback_query_handler(text_contains='b0')
async def group_11O(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    
    lessons = readDataShankursky('src\\crawler\\data\\Shankursky\\file1_course_Shankursky.xlsx', 'Лист1')[0]
    lessons = [lesson if lesson is not None else "Нет предметов" for lesson in lessons]

    mondayLessons = '\n'.join([f"▫️ {i+1}. {lesson}" for i, lesson in enumerate(lessons)])
    tuesdayLessons = '\n'.join([f"▫️ {i+2}.{lesson}" for i, lesson in enumerate(lessons)])
    wednesdayLessons = '\n'.join([f"▫️ {i+3}.{lesson}" for i, lesson in enumerate(lessons)])
    thursdayLessons = '\n'.join([f"▫️ {i+4}.{lesson}" for i, lesson in enumerate(lessons)])
    fridayLessons = '\n'.join([f"▫️ {i+5}.{lesson}" for i, lesson in enumerate(lessons)])

    await bot.send_message(call.from_user.id, f'''👤 Группа 11O\n\n📋 Расписание:\n\n📕Понедельник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{mondayLessons}
                           \n📗Вторник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{tuesdayLessons}
                           \n📘Среда\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{wednesdayLessons}
                           \n📙Четверг\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{thursdayLessons}
                           \n📔Пятница\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{fridayLessons}''', reply_markup=groups.defaultGroups())
    

@dp.callback_query_handler(text_contains='b1')
async def group_11O(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    lessons = readDataShankursky('src\\crawler\\data\\Shankursky\\file1_course_Shankursky.xlsx', 'Лист1')[1]
    lessons = [lesson if lesson is not None else "Нет предметов" for lesson in lessons]

    mondayLessons = '\n'.join([f"▫️ {i+1}. {lesson}" for i, lesson in enumerate(lessons)])
    tuesdayLessons = '\n'.join([f"▫️ {i+2}.{lesson}" for i, lesson in enumerate(lessons)])
    wednesdayLessons = '\n'.join([f"▫️ {i+3}.{lesson}" for i, lesson in enumerate(lessons)])
    thursdayLessons = '\n'.join([f"▫️ {i+4}.{lesson}" for i, lesson in enumerate(lessons)])
    fridayLessons = '\n'.join([f"▫️ {i+5}.{lesson}" for i, lesson in enumerate(lessons)])

    await bot.send_message(call.from_user.id, f'''👤 Группа 32ИС\n\n📋 Расписание:\n\n📕Понедельник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{mondayLessons}
                           \n📗Вторник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{tuesdayLessons}
                           \n📘Среда\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{wednesdayLessons}
                           \n📙Четверг\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{thursdayLessons}
                           \n📔Пятница\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{fridayLessons}''', reply_markup=groups.defaultGroups())
    

@dp.callback_query_handler(text_contains='b2')
async def group_11O(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    lessons = readDataShankursky('src\\crawler\\data\\Shankursky\\file1_course_Shankursky.xlsx', 'Лист1')[2]
    lessons = [lesson if lesson is not None else "Нет предметов" for lesson in lessons]

    mondayLessons = '\n'.join([f"▫️ {i+1}. {lesson}" for i, lesson in enumerate(lessons)])
    tuesdayLessons = '\n'.join([f"▫️ {i+2}.{lesson}" for i, lesson in enumerate(lessons)])
    wednesdayLessons = '\n'.join([f"▫️ {i+3}.{lesson}" for i, lesson in enumerate(lessons)])
    thursdayLessons = '\n'.join([f"▫️ {i+4}.{lesson}" for i, lesson in enumerate(lessons)])
    fridayLessons = '\n'.join([f"▫️ {i+5}.{lesson}" for i, lesson in enumerate(lessons)])

    await bot.send_message(call.from_user.id, f'''👤 Группа 32ИС(д)\n\n📋 Расписание:\n\n📕Понедельник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{mondayLessons}
                           \n📗Вторник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{tuesdayLessons}
                           \n📘Среда\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{wednesdayLessons}
                           \n📙Четверг\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{thursdayLessons}
                           \n📔Пятница\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{fridayLessons}''', reply_markup=groups.defaultGroups())


@dp.callback_query_handler(text_contains='b3')
async def group_11O(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    lessons = readDataShankursky('src\\crawler\\data\\Shankursky\\file1_course_Shankursky.xlsx', 'Лист1')[3]
    lessons = [lesson if lesson is not None else "Нет предметов" for lesson in lessons]

    mondayLessons = '\n'.join([f"▫️ {i+1}. {lesson}" for i, lesson in enumerate(lessons)])
    tuesdayLessons = '\n'.join([f"▫️ {i+2}.{lesson}" for i, lesson in enumerate(lessons)])
    wednesdayLessons = '\n'.join([f"▫️ {i+3}.{lesson}" for i, lesson in enumerate(lessons)])
    thursdayLessons = '\n'.join([f"▫️ {i+4}.{lesson}" for i, lesson in enumerate(lessons)])
    fridayLessons = '\n'.join([f"▫️ {i+5}.{lesson}" for i, lesson in enumerate(lessons)])

    await bot.send_message(call.from_user.id, f'''👤 Группа 21ИС\n\n📋 Расписание:\n\n📕Понедельник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{mondayLessons}
                           \n📗Вторник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{tuesdayLessons}
                           \n📘Среда\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{wednesdayLessons}
                           \n📙Четверг\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{thursdayLessons}
                           \n📔Пятница\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{fridayLessons}''', reply_markup=groups.defaultGroups())
    
@dp.callback_query_handler(text_contains='b4')
async def group_11O(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    lessons = readDataShankursky('src\\crawler\\data\\Shankursky\\file1_course_Shankursky.xlsx', 'Лист1')[4]
    lessons = [lesson if lesson is not None else "Нет предметов" for lesson in lessons]

    mondayLessons = '\n'.join([f"▫️ {i+1}. {lesson}" for i, lesson in enumerate(lessons)])
    tuesdayLessons = '\n'.join([f"▫️ {i+2}.{lesson}" for i, lesson in enumerate(lessons)])
    wednesdayLessons = '\n'.join([f"▫️ {i+3}.{lesson}" for i, lesson in enumerate(lessons)])
    thursdayLessons = '\n'.join([f"▫️ {i+4}.{lesson}" for i, lesson in enumerate(lessons)])
    fridayLessons = '\n'.join([f"▫️ {i+5}.{lesson}" for i, lesson in enumerate(lessons)])

    await bot.send_message(call.from_user.id, f'''👤 Группа 1ИС\n\n📋 Расписание:\n\n📕Понедельник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{mondayLessons}
                           \n📗Вторник\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{tuesdayLessons}
                           \n📘Среда\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{wednesdayLessons}
                           \n📙Четверг\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{thursdayLessons}
                           \n📔Пятница\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n{fridayLessons}''', reply_markup=groups.defaultGroups())


@dp.message_handler(commands=['test'])
async def start_message(message: types.Message):
    await message.answer('Режим теста', reply_markup=menu.menu)
    await message.answer(readDataShankursky('src\\crawler\\data\\Shankursky\\file1_course_Shankursky.xlsx', 'Лист1'), reply_markup=groups.choiceGroupKB)




   