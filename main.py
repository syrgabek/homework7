import asyncio

from aiogram import executor
from bot_instance import dp
from handers import client, callback, extra, fsmadmin, notification, inline
from database import bot_db
from handers.notification import scheduler

"""
heroku logs --tail --app (название вашего приложения)
heroku ps:scale worker=1
heroku ps:scale worker=0 
"""


async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(scheduler())
    print("Bot is online")


fsmadmin.register_handler_fsmadmin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
inline.register_handlers_inline(dp)
extra.register_handlers_extra(dp)
notification.register_handler_notification(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
