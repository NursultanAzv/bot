from aiogram import types, Dispatcher
from config import bot, ADMINS
from asyncio import sleep
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def ban(message: types.Message):
    if message.chat.type == "group":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан "
                                 f"забанил {message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")




async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id, f"id - {user['id']},\n"
                                                     f"имя - {user['name']},\nнаправление - {user['direction']},\n"
                                                     f"возраст - {user['age']}, \n "
                                                     f"группа - {user['group']}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"Удалить {user[1]}", callback_data=f"delete {user[0]}")))


async def delete_user(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id,
                               f"id - {user[0]},name - {user[1]},dir - {user[2]}, "
                               f"age - {user[3]}, group - {user[4]}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"Delete {user[1]}", callback_data=f"delete {user[0]}")
                               ))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(int(call.data.replace('delete ', '')))
    await call.answer(text="Стёрт с базы данных", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_message_admin(dp: Dispatcher):
    dp.register_message_handler(delete_user, commands=["del"])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")
    # dp.register_message_handler(random_game)
