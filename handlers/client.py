from aiogram import Dispatcher, types
from config import dp, bot, ADMINS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.client_kb import start_markup
from asyncio import sleep
from database.bot_db import sql_command_random, sql_command_all
from parser.parser_wheel import parser


async def start_handler(message: types.Message):
    await message.answer(f"Привет {message.from_user.username}\n"
                         f"Мемы? /mem\n"
                         f"Викторину? нажми /quiz\n"
                         f"Хочешь возвести какое-то число в квадрат, просто напиши это число\n"
                         f"Хочешь покидать кости с ботом нажми /dice\n"
                         f"Дайвинчик? /reg\n"
                         f"Регистрация ментора? /reg_ment\n"
                         f"Запарсить сайт? /wheel")

#
# # @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     await bot.send_message(message.from_user.id,
#                            f"Hello  {message.from_user.first_name}",
#                            reply_markup=start_markup)


# @dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    photo = open("../hw_bot1/media/zzz.jpeg", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "2 + 2 = ?"
    answers = [
        "1",
        "22",
        "4",
        "5",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="мдаа",
        open_period=10,
        reply_markup=markup
    )


async def dice(message: types.Message):
    await bot.send_message(message.from_user.id, f"Играем в кости!")
    await sleep(1)

    await bot.send_message(message.from_user.id, f"Ход бота")
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(4)

    await bot.send_message(message.from_user.id, f"Твой ход")
    user_data = await bot.send_dice(message.from_user.id, "Твой ход")
    user_data = user_data['dice']['value']
    await sleep(4)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, "Ты проиграл(")
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, "Ты выиграл)")
    else:
        await bot.send_message(message.from_user.id, "Ничья")


async def pin_message(message: types.Message):
    if message.chat.type == "group" and message.from_user.id in ADMINS:
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        else:
            await message.answer("Cообщение должно быть ответом")


async def get_random_user(message: types.Message):
    # await message.answer("Какое направление?", reply_markup=direction_markup)
    await sql_command_random(message)


async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
        )


async def get_all_mentor(message: types.Message):
    await sql_command_all()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(send_meme, commands=['meme'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(dice, commands=['dice'], commands_prefix="!/")
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix="!")
    dp.register_message_handler(get_random_user, commands=["getmentor"])
    dp.register_message_handler(get_all_mentor, commands=["allmentor"])
    dp.register_message_handler(parsser_wheels, commands=["wheel"])
