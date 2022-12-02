from aiogram import types, Dispatcher
from config import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# @dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Kyrgyzstan get independence in ? year"
    answers = [
        "1992",
        "2020",
        "1991",
        "1946",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="мдаа",
        open_period=10,
        reply_markup=markup

    )


async def quiz_3(call: types.CallbackQuery):
    question = "3 + 3 = ?"
    answers = [
        "2",
        "6",
        "12",
        "33",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="мдаа",
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text=['button_call_1'])
    dp.register_callback_query_handler(quiz_3, text=['button_call_2'])

