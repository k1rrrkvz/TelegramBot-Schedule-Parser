import os 
from aiogram import Bot, Dispatcher
from data import config


bot = Bot(token=config.TOKEN, parse_mode = 'html')
dp = Dispatcher(bot)


