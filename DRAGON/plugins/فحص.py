import sys
import time
from datetime import datetime
import requests
from telethon import __version__ as __tele_version__
from telethon import events, TelegramClient
from DRAGON import DRAGON, StartTime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

__python_version__ = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}"


@DRAGON.on(events.NewMessage(outgoing=True, pattern=f"^.فحص$"))
async def alive_t(event):
    start = datetime.now()
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[۩▬▬ DRAGON USERBOT ▬▬۩](https://t.me/Dragon_2022_D)**\n━━━━━━━━━━━━━━━━━━\n"
    reply_msg += f"أصدار البايثون: `{__python_version__}`\n"
    reply_msg += f"أصدار التيليثون: `{__tele_version__}`\n"
    reply_msg += f"أصدار دراكون:** `0.1`**\n"
    reply_msg += f"━━━━━━━━━━━━━━━━━━"
    end_time = time.time()
    reply_msg += f"\n- الوقت: {uptime}"
    await event.edit(reply_msg)

@DRAGON.on(events.NewMessage(outgoing=True, pattern=f"^.بنك$"))
async def _(event):
    app_info = await DRAGON.get_me()
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"• DRAGON USERBOT •\n\n<b>- سرعة البنك<b/>: <code>{ms} في الثانيه</code>", parse_mode="html")
