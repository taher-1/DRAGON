from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 

@borg.on(admin_cmd(pattern=r"صمون"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("صمون")

    animation_chars = [
        
            "🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖",
            "🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖",
            "🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖",
            "🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖",
            "🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖",    
            "🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖",
            "🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖\n🥖صمووون 10 بالف صمووون🥖",
            "🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖",
            "🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖",
            "🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖",
            "🥖صمووون 10 بالف صمووون🥖\n🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖\n🥖صمووون 10 بالف صمووون🥖",
            "[ **صمووون 10 بالف صمووون**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
