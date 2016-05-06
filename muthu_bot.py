import asyncio
import os
import configparser
import telepot.async
from credentials import get_telegram_bot_api_key
from muthu_tasks import execute_task


@asyncio.coroutine
def handle(msg_packet):
    chat_id, response_text = execute_task(msg_packet)
    if response_text != '':
        yield from bot.sendMessage(chat_id, response_text)


telegram_bot_api_key = get_telegram_bot_api_key()

bot = telepot.async.Bot(telegram_bot_api_key)
loop = asyncio.get_event_loop()

loop.create_task(bot.message_loop(handle))

loop.run_forever()