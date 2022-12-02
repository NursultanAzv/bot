from aiogram import executor
from config import dp
import logging
from handlers import client, callback, admin, extra, FSM_admin_mentors, notification
import asyncio
from database.bot_db import *
async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
FSM_admin_mentors.register_handlers_fsm_anketa(dp)
# extra.register_handlers_extra(dp)
notification.register_handlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
