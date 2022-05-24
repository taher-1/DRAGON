import asyncio
from telethon import events
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest
from DRAGON import DRAGON

@DRAGON.on(events.NewMessage(outgoing=True, pattern="^.ضيف$"))
async def get_users(event):
    legen_ = event.text[10:]
    DRAGON_chat = legen_.lower
    restricted = ["@T2R_3", "@T2R_3"]
    DRAGON = await event.edit(f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    if DRAGON_chat in restricted:
        return await DRAGON.edit(
            event, "**- لا يمكنك اخذ الاعضاء من مجموعه السورس العب بعيد ابني  :)**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await DRAGON.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    else:
        await DRAGON.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    if event.is_private:
        return await DRAGON.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await DRAGON.edit(
        "**▾∮ حالة الأضافة:**\n\n**▾∮ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await DRAGON.edit(
                    f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await DRAGON(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await DRAGON.edit(
                f"**▾∮تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await DRAGON.edit(
        f"**▾∮اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`"
    )
