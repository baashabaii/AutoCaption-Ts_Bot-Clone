import os, asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["TG_BOT_TOKEN"],
    api_id = int(os.environ["APP_ID"]),
    api_hash = os.environ["API_HASH"]
)


@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
            await m.delete()
        else:
            await m.copy(m.chat.id)
            await m.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)


@bot.on_message(filters.private | filters.group)
async def fwdrm(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
        else:
            await m.copy(m.chat.id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
