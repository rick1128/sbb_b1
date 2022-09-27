import re

from telethon import Button, events
from telethon.events import CallbackQuery

from sbb_b import sbb_b 
from ..core import check_owner
from ..Config import Config
from razan.CMD import *

ROE = "** هـذه هي قائمة اوامـر سـورس جمثون **"
ROZADM = "من هنا يمكنك ايجاد جميع"
RAZAN = Config.TG_BOT_USERNAME

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                [Button.inline("معلومات جمثون", data="AOMRDB")],
                [
                    Button.inline("البوت", data="eeeeq"),
                    Button.inline("الكروب", data="admincmd_s")
                ],
                [
                    Button.inline("التسلية", data="TASLIACMD"),
                    Button.inline("الاداوات", data="toolsed"),
                ],
                [
                    Button.inline("متفرقات", data="tslrzj"),
                    Button.inline(" الترحيبات والردود ", data="r7brz"),
                ],
                [
                    Button.inline("الاكسترا", data="krrznd"),
                    Button.inline(" الفارات", data="jrzst"),
                ]
            ]
            result = builder.article(
                title="sbb_b",
                text=ROE,
                buttons=buttons,
                link_preview=False,
            )
        await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
#@sbb_b.ar_cmd(pattern="اوامري")
async def repo(event):
    if event.fwd_from:
        return
    start = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(start, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MAIN")))
@check_owner
async def _(event):
    butze = [
                [Button.inline("معلومات جمثون", data="AOMRDB")],
                [
                    Button.inline("البوت", data="sssss"),
                    Button.inline("الكروب", data="admincmd_s")
                ],
                [
                    Button.inline("التسلية", data="TASLIACMD"),
                    Button.inline("الاداوات", data="toolsed"),
                ],
                [
                    Button.inline("متفرقات", data="tslrzj"),
                    Button.inline(" الترحيبات والردود ", data="r7brz"),
                ],
                [
                    Button.inline("الاكسترا", data="krrznd"),
                    Button.inline(" الفارات", data="jrzst"),
                ]
    ]
    await event.edit(ROE, buttons=butze)



@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"toolsed1")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("اذاعة للخاص", data="BROADEV1"),
    Button.inline("اذاعة للكروب", data="BRWAADV1"),
    Button.inline("اضافة اعضاء", data="ADDMEM7"),
    ],
    [
    Button.inline("الانتحال", data="CLIONEACMD"),
    Button.inline("الاعادة", data="ALIBACK"),
    Button.inline("التحديث", data="UPDATE4E"),
    ],
    [
    Button.inline("ايدي", data="KSHFCMD"),
    Button.inline("التقليد", data="ADDTKLED"),
    Button.inline("ايقاف التقليد", data="STOPAZAG"),
    ],
    [Button.inline("التالي", data="TOOLCMD2"),
     Button.inline("رجوع", data="jrzst")
     ],
     [
     Button.inline("القائمة الرئيسية", data="MAIN")
     ]]
    await event.edit(ROE, buttons=buttons)

#######################################################################

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOOLCMD2")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("المقلدهم", data="ALMKD5D"),
    Button.inline("حذف المقلدهم", data="NOAZAJ4"),
    Button.inline("تلكراف ميديا", data="TELEHTMED"),
    ],
    [
    Button.inline("كرر", data="TKRAR3ADI"),
    Button.inline("بوت نشر (مكرر)", data="MKRRR5"),
    Button.inline("سبام", data="SPAM3AAH"),
    ],
    [
    Button.inline("ايقاف التكرار", data="KSHFCMD"),
    Button.inline("وسبام", data="FGKHEF8"),
    Button.inline("تلكراف ميديا", data="TELEHTMED"),
    ],
    [Button.inline("التالي", data="admin2"),
     Button.inline("رجوع", data="jrzst")
     ],
     [
     Button.inline("القائمة الرئيسية", data="MAIN")
     ]]
    await event.edit(ROE, buttons=buttons)



@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMKD5D")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALMKD5D, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"NOAZAJ4")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(NOAZAJ4, buttons=buttons)

#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TELEHTMED")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(TELEHTMED, buttons=buttons)

#TELEHTMED

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TKRAR3ADI")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(TKRAR3ADI, buttons=buttons)

#ثثثث

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MKRRR5")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(MKRRR5, buttons=buttons)

#ويو جوا 

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"FGKHEF8")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(FGKHEF8, buttons=buttons)

#اي

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SPAM3AAH")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(SPAM3AAH, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TELEHTMED")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(TELEHTMED, buttons=buttons)

######

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BROADEV1")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(BROADEV1, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BRWAADV1")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(BRWAADV1, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"CLIONEACMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(CLIONEACMD, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIBACK")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIBACK, buttons=buttons)

#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"UPDATE4E")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(UPDATE4E, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KSHFCMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(KSHFCMD, buttons=buttons)

#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADDTKLED")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ADDTKLED, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STOPAZAG")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="toolsed1")]]
    await event.edit(TSLEACMD, buttons=buttons)


##


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TASLIACMD")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("الترفيه", data="TRFEHCMD"),
    Button.inline("التسلية", data="TSLEACMD"),
    ],
    [
     Button.inline("القائمة الرئيسية", data="MAIN")
     ]
     ]
    await event.edit(ROE, buttons=buttons)



@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TSLEACMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="TASLIACMD")]]
    await event.edit(TSLEACMD, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TRFEHCMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="TASLIACMD")]]
    await event.edit(ALTKRARCMD, buttons=buttons)



@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admincmd_s")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("حظر", data="bancmd"),
    Button.inline("الغاء حظر", data="unbancmd"),
    Button.inline("المحظورين", data="ALIVEMHA"),
    ],
    [
    Button.inline("كتم", data="bancmd"),
    Button.inline("الغاء كتم", data="unmutecmd"),
    Button.inline("طرد", data="KICKCMD"),
    ],
    [
    Button.inline("تثبيت", data="ALIVEbin"),
    Button.inline("الغاء التثبيت", data="ALIVEunbin"),
    Button.inline("رفع مشرف", data="ALIVEadmin"),
    ],
    [Button.inline("التالي", data="admin2"),
     Button.inline("رجوع", data="jrzst")
     ]]
    await event.edit(ROE, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admin2")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("تنزيل مشرف", data="ALIVEtnadmin"),
    Button.inline("وضع صورة", data="ALIVEsod"),
    Button.inline("حذف الصورة", data="ALIVESOR"),
    ],
    [
    Button.inline("ارفع", data="ALIVErfe"),
    Button.inline("نزل", data="ALIVEnzl"),
    Button.inline("الاحداث", data="ALIVEADV"),
    ],
    [
    Button.inline("تفليش", data="ALIVETFL"),
    Button.inline("تنزيل الكل", data="ALIVEgma"),
    Button.inline("تحذير", data="ALIVETHR"),
    ],
    [Button.inline("التالي", data="admi3"),
     Button.inline("رجوع", data="admincmd_s")
     ]]
    await event.edit(ROE, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admi3")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("حذف التحذيرات", data="ALIVEunTHR"),
    Button.inline("التحذيرات", data="ALIVETSV"),
    Button.inline("اضافة ترحيب", data="ALIVETRSB"),
    ],
    [
    Button.inline("ايقاف الترحيب", data="ALIVEundf"),
    Button.inline("الترحيبات", data="ALIVETRS"),
    Button.inline("منع كلمة", data="ALIVEADV"),
    ],
    [
    Button.inline("الغاء منع", data="A3ALMN3"),
    Button.inline("قائمة المنع", data="ALIVEgma"),
    Button.inline("مسح المحظورين", data="UMBLCTR"),
    ],
    [Button.inline("التالي", data="ADMSS4"),
     Button.inline("رجوع", data="admin2")
     ]]
    await event.edit(ROE, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADMSS4")))
@check_owner
async def _(event):
    buttons = [
    [
    Button.inline("اضافة رد", data="RDAJFDA"),
    Button.inline("ايقاف رد", data="RSTOPRD"),
    Button.inline("حذف الردود", data="ALLRDSTOP"),
    ],
    [
    Button.inline("الردود", data="ALLRD5"),
    Button.inline("احصائيات", data="ALMSHRFE1"),
    Button.inline("اطردني", data="MELICLW"),
    ],
    [
    Button.inline("المحذوفين", data="ACCD5SS"),
    Button.inline("ضع التكرار", data="ALTKRARCMD"),
    ],
    [Button.inline("التالي", data="admincmd_s"),
     Button.inline("رجوع", data="admi3")
     ]]
    await event.edit(ROE, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALTKRARCMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALTKRARCMD, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ACCD5SS")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ACCD5SS, buttons=buttons)



@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMSHRFE1")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALMSHRFE1, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRS")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALIVETRS, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MELICLW")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(MELICLW, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALLRD5")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALLRD5, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALLRDSTOP")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALLRDSTOP, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"RSTOPRD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(RSTOPRD, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"RDAJFDA")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(RDAJFDA, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"UMBLCTR")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(UMBLCTR, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"LISTBLCK")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(LISTBLCK, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"A3ALMN3")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(A3ALMN3, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMN3CMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(ALMN3CMD, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRS")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETRS, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEundf")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVEundf, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRSB")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETRSB, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETSV")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETSV, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEunTHR")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVEunTHR, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETHR")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVETHR, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEgma")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEgma, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEADV")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEADV, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVErfe")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVErfe, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEnzl")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEnzl, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEnzl")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVESOR, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEsod")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEsod, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEbin")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEtnadmin, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEbin")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEbin, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEunbin")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEunbin, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEadmin")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEadmin, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KICKCMD")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEMHA, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEMHA")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEMHA, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"bancmd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEBand, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"unbancmd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEunban, buttons=buttons)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"mutecmd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEcatm, buttons=buttons)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"unmutecmd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEuncatm, buttons=buttons)
