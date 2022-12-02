from aiogram import types, Dispatcher
from config import dp, bot, ADMINS
import random


# @dp.message_handler()
async def echo(message: types.Message):
    # async def random_game(message: types.Message):
    # if message.chat.type == "group" and message.from_user.id in ADMINS:
    emoji = ['🎲', '🎯', '🎳', '🎰']
    if message.text.startswith("game"):
        await bot.send_dice(message.from_user.id, emoji=random.choice(emoji))


    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text * 2)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
