from ..core.session import sbb_b
@sbb_b.on(admin_cmd(pattern="ليمونة(?: |$)(.*)"))
async def _(event):    
    await event.edit("🍋 هاك حطه بطيرك")

@sbb_b.on(admin_cmd(pattern="دي(?: |$)(.*)"))
async def _(event):    
    await event.edit("ولي منا فرخ")
