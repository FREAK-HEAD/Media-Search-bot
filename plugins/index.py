import pytz
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import InviteHashExpired, UserAlreadyParticipant
from config import Config
import re
from bot import Bot
from asyncio.exceptions import TimeoutError
from database import save_data
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.ERROR)

limit_no=""               
skip_no=""
caption=""
channel_type=""
channel_id_=""
IST = pytz.timezone('Asia/Kolkata')
OWNER=int(Config.OWNER_ID)


@Client.on_message(filters.private & filters.command(["index"]))
async def run(bot, message):
    if message.from_user.id != OWNER:
        await message.reply_text("Who the hell are you!!")
        return
    while True:
        try:
            chat = await bot.ask(text = "To Index a channel you may send me the channel invite link, so that I can join channel and index the files.\n\nIt should be something like <code>https://t.me/xxxxxx</code> or <code>https://t.me/joinchat/xxxxxx</code>", chat_id = message.from_user.id, filters=filters.text, timeout=30)
            channel=chat.text
        except TimeoutError:
            await bot.send_message(message.from_user.id, "Error!!\n\nRequest timed out.\nRestart by using /index")
            return

        pattern=".*https://t.me/.*"
        result = re.match(pattern, channel, flags=re.IGNORECASE)
        if result:
            print(channel)
            break
        else:
            await chat.reply_text("Wrong URL")
            continue

    if 'joinchat' in channel:
        global channel_type
        channel_type="private"
        try:
            await bot.USER.join_chat(channel)
        except UserAlreadyParticipant:
            pass
        except InviteHashExpired:
            await chat.reply_text("Wrong URL or User Banned in channel.")
            return
        while True:
            try:
                id = await bot.ask(text = "Since this is a Private channel I need Channel id, Please send me channel ID\n\nIt should be something like <code>-100xxxxxxxxx</code>", chat_id = message.from_user.id, filters=filters.text, timeout=30)
                channel=id.text
            except TimeoutError:
                await bot.send_message(message.from_user.id, "Error!!\n\nRequest timed out.\nRestart by using /index")
                return
            channel=id.text
            if channel.startswith("-100"):
                global channel_id_
                channel_id_=int(channel)
                break
            else:
                await chat.reply_text("Wrong Channel ID")
                continue

    except Exception as e:
        print(e)
        await m.edit(text=f"Error: {e}")
        pass
