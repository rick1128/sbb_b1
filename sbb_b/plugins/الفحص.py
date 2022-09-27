import random
import re
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from sbb_b import StartTime, jmthonversion, sbb_b

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time, jmthonalive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention


@sbb_b.ar_cmd(pattern="فحص$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    ANIME = None
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    if "ANIME" in jmthon_caption:
        data = requests.get("https://animechan.vercel.app/api/random").json()
        ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    jmthonevent = await edit_or_reply(event, "**- جار التأكد انتظر قليلا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**سورس ريكثون يعمل بنجاح**"
    JMTHON_IMG = gvarstatus("ALIVE_PIC")
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=jmthonversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if JMTHON_IMG:
        JMTHON = list(JMTHON_IMG.split())
        PIC = random.choice(JMTHON)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await jmthonevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                jmthonevent,
                f"**رابط الصورة غير صحيح**\nعليك الرد على رابط الصورة ب .اضف صورة الفحص",
            )
    else:
        await edit_or_reply(
            jmthonevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} قاعدة البيانات :** `{dbhealth}`
**{EMOJI} اصدار التيليثون:** `{telever}`
**{EMOJI} اصدار ريكثون :** `{jmver}`
**{EMOJI} اصدار البايثون :** `{pyver}`
**{EMOJI} الوقت :** `{uptime}`
**{EMOJI} المالك:** {mention}"""


def jmthonalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    jmthon_caption = "**سورس ريكثون يعمل بنجاح**\n"
    jmthon_caption += f"**{EMOJI} اصدار التيليثون :** `{version.__version__}\n`"
    jmthon_caption += f"**{EMOJI} اصدار ريكثون :** `{jmthonversion}`\n"
    jmthon_caption += f"**{EMOJI} اصدار البايثون :** `{python_version()}\n`"
    jmthon_caption += f"**{EMOJI} المالك:** {mention}\n"
    return jmthon_caption


@sbb_b.ar_cmd(pattern="السورس$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, "ألسورس")
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await jmthonalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
