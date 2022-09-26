from . import *


@sbb_b.ar_cmd(pattern="حفظ كتابة$")
async def save(e):
    razan = await e.get_reply_message()
    if not razan:
        return await edit_delete(
            e, "- يجب عليك اولا الرد على الرسالة لحفظها في الرسائل المحفوظة", time=8
        )
    if e.out:
        await e.client.send_message("me", razan)
    else:
        await e.client.send_message(e.sender_id, razan)
    await edit_delete(e, "- تم بنجاح حفظ الرسالة في الرسائل المحفوظة", time=8)


@sbb_b.ar_cmd(pattern="حفظ توجيه$")
async def saf(e):
    razan = await e.get_reply_message()
    if not razan:
        return await edit_delete(
            e, "- يجب عليك اولا الرد على الرسالة لحفظها في الرسائل المحفوظة", time=8
        )
    if e.out:
        await razan.forward_to("me")
    else:
        await razan.forward_to(e.sender_id)
    await edit_delete(e, "- تم بنجاح حفظ الرسالة في الرسائل المحفوظة", time=8)
