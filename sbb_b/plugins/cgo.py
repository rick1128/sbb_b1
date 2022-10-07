from ..core.session import sbb_b
@sbb_b.on(admin_cmd(pattern="فحصص(?: |$)(.*)"))
async def _(event):    
    await event.edit("{jmver}")
