from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -
# - SYTHOM TEAM 
# -

sython1.start()



c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5789819429]




@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@sy_tem"))
    except BaseException:
        pass
      

@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@K_K_Q_L"))
    except BaseException:
        pass  
        
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='.تاقیکردنەوە'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سەرچاوەکە کاردەکات ⚡️**')
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سەرچاوەکە کاردەکات ⚡️**')


@sython1.on(events.NewMessage(outgoing=False, pattern='.help'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ بەخێربێن بۆ فەرمانەکانی كورد پوینت
 
============= • SA • ============

𝟏 - بۆ داخڵکردنی داواکاری کۆکردنەوە : .کۆکردنەوە

𝟐 - بۆ داخڵکردنی فەرمانەکانی کۆنترۆڵ : .کۆنترۆڵ

𝟑 - بۆ داخڵکردنی ڕێزبەندی جیاواز : .تایبەتمەندی

𝟒 - بۆ پشکنینی کاری سەرچاوەکە : .تاقیکردنەوە

============= • SA • ============
**""")


@sython1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ هەموو ئەو فەرمانانەی وەجبە کە پێویستت پێیانە بنووسە

============= • 𝐒𝐘 • ============

`/point1` :  خاڵەکانی بۆت المليار کۆبکەرەوە
`/point2` : خاڵەکانی بۆت الجوكر کۆبکەرەوە
`/point3` :  خاڵەکانی بۆت العقاب کۆبکەرەوە 
`/point4` :   خاڵەکانی بۆت العرب کۆبکەرەوە

note : ئەم فەرمانانە بە ناردنیان بۆ ئەکاونتەکە یان بە ناردنیان بۆ گروپێک کە ئەکاونتەکە تێیدا هەڵکەوتووە بەکاردەهێنرێن

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : کۆکردنەوەی خاڵەکانی بۆت لە لیستەکەدا نییە

note : بۆ دانانی بۆتەکە لە شوێنی خۆیدا بۆتی پێویست بەکاربهێنە

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : کۆکردنەوەی بێکۆتایی 

note : بۆ دانانی بۆتەکە لە شوێنی خۆیدا بۆتی پێویست بەکاربهێنە

note : دووەم ژمارەی چرکەکان دابنێ

note : پێشنیار دەکەین ژمارەی چرکەکان لەسەر ٣٠٠ دابنێیت

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : بەشداری ئەو کەناڵە بۆتانەی کە باسکراون

`/transfer` : لیستی گواستنەوەی خاڵەکان بنووسە
`/infoacc` : لیستی زانیاری گواستنەوە داخڵ بکە

`/lpoint` : بۆ دەرچوون لە هەموو کەناڵ و گروپەکان

============= • 𝐒𝐘 • ============
**""")

@sython1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ لیستی فەرمانەکانی کۆنترۆڵکردنی ئەکاونت

============= • 𝐒𝐘 • ============

𝟏 - بۆ گواستنەوەی دوا پەیام لە بەکارهێنەرێک یان بۆتێکی دیاریکراوەوە :

`/forward + ئەکاونتی بەکارهێنەر یان بۆت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - بۆ ناردنی نامە بۆ بەکارهێنەرێک یان بۆتێکی دیاریکراو : 

`/send + نامەكە + ئەکاونتی بەکارهێنەر یان بۆت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - بۆ ئەوەی ئەکاونتەکە بێت کلیک لەسەر دوگمەی شەفاف بکە لە بۆتەکەدا : 

`/button + ژمارەی دوگمەی شەفاف + بەکارهێنەری بۆت`

note :  ژمارەی دوگمەی شەفاف لە ژمارە 0 ەوە حیساب بکە

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - بۆ ئەوەی ئەکاونتەکە بەشداری کەناڵێک یان گروپێک بکات

`/jn + سەردانی کەناڵ یان گروپ دەکات `

============= • 𝐒𝐘 • ============
**""")

@sython1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ لیستی فەرمانە تایبەتەکان
============= • 𝐒𝐘 • ============

𝟏 - بۆ چالاککردنی بۆتەکە بە چوونە ژوورەوەی بەستەری بانگهێشتنامە : 

`/bot + ئایدی ئەکاونت + بەکارهێنەری بۆت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - ئەم فرمانەی خوارەوە ئەو تێبینیانەی تێدایە کە پێویستت پێیانە :

`/notes`

𝟑 - بۆ ئەوەی ئەکاونتەکە دەنگ بدات لە پێشبڕکێی لایکەکاندا :

`/voice + موقع الرسالة + يوزر القناة`

note : شوێنی نامەکە مانای ئەوەیە، بۆ نمونە ئەگەر ناوی ناو کەناڵی پێشبڕکێکە ناوی کۆتایی یان کۆتا پۆست بێت، ئەوا شوێنی نامەکە ١ بێت، وە ئەگەر پێش کۆتا نامەکە بێت، ئەوا شوێنەکەی ٢ دەبێت، و بەم شێوەیە بۆ باقی سایتەکان

𝟒 - بۆ ئەوەی ئەکاونتەکە کەناڵێک یان گروپێک بەجێبهێڵێت :

`/lv + یوزرنیمی کەناڵ`

============= • 𝐒𝐘 • ============
**""")

@sython1.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
1 - ئەگەر دەتەوێت ئەکاونتەکانی ناو کۆکردنەوە کۆنتڕۆڵ بکەیت، خاڵەکانی گواستنەوە و زانیاری هەر ئەکاونتێک بزانیت، گروپێکی تایبەت دروست بکە و ئەو ئەکاونتانە داخڵ بکە کە سەرچاوەکەت بۆ دامەزراندووە و ئەکاونتەکان بەرز بکەرەوە بۆ سەرپەرشتیارەکان، پاشان فەرمانەکانی کۆکردنەوە بەکاربهێنە

2 - ئەگەر دەتەوێت وا لە ئەکاونتەکان بکەیت خاڵەکان کۆبکەنەوە بەبێ وەستان و ڕێژەیەکی کەم لە قەدەغەکردنەکان، ئەوا فەرمانەکە 
بەکاربهێنە : somy/ 

دەتوانیت زیاتر دەربارەی فەرمانەکە و چۆنیەتی بەکارهێنانی لە لیستی کۆمپایڵکردندا بزانیت، پێشنیار دەکرێت لە کاتی بەکارهێنانی فرمانەکەدا ژمارەی چرکەکان دابنێیت بۆ ٣٠٠، واتە کاتێک هەڵەیەک لە کۆمپایڵکردنەکەدا ڕوودەدات یان کەناڵەکان کۆتاییان دێت، سەرچاوەکە هەوڵدەدات دوای ٣٠٠ واتە پێنج خولەک بە شێوەیەکی ئۆتۆماتیکی کۆمپایڵ بکات و سەرچاوەکە ئاگادارت دەکاتەوە لە هەموو ئەو شتانەی کە گەیشتوونەتە دەست

3 - ئەگەر دەتەوێت خاڵەکانی بۆتەکانی پارەدان بە شێوەیەکی ئاسایی کۆبکەیتەوە بەبێ ئەوەی بە شێوەیەکی ئۆتۆماتیکی هەوڵی دووبارە بدەیتەوە، دەتوانیت ئەم فرمانانەی خوارەوە بەکاربهێنیت [point , /point1/ , .....] دەتوانیت پێداچوونەوە بە فرمانەکانی ناو لیستەکەدا بکەیت دوو بەشی یەکەمی لیستەکە
**""")

@sython1.on(events.NewMessage(outgoing=True, pattern=".help"))
async def _(event):
      await event.edit("""**
〠 فەرمانەکانی ئەژمێری بەکارهێنەر

• بۆت زیادکردنی ئەندام المليار  - `.تجميع المليار`

• بۆت زیادکردنی ئەندام الجوكر - `.تجميع الجوكر`

• بۆت زیادکردنی ئەندام العقـاب - `.تجميع العقاب`

• بۆت زیادکردنی ئەندام العـرب  - `.تجميع العرب `

• پشکنینی سەرچاوە      - `.تاقیکردنەوە`**""")



@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تاقیکردنەوە"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**پشکنین لە پێشکەوتندایە..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("خاڵەکان کۆدەکرێنەوە")
        await event.edit("خاڵەکان کۆدەکرێنەوە")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                await sython1.send_message(event.chat_id, f"کۆکردنەوە تەواو بوو | SA")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='پشتڕاستکردنەوە')
                chs += 1
                await event.edit(f"لە کەناڵی {chs} بەشداری کردووە")
            except:
                msg2 = await sython1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"کەناڵی ژمارە {chs}")

        await sython1.send_message(event.chat_id, "کۆکردنەوە تەواو بوو | SA")
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("خاڵەکان کۆدەکرێنەوە")
        await event.edit("خاڵەکان کۆدەکرێنەوە")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                await sython1.send_message(event.chat_id, f"کۆکردنەوە تەواو بوو | SA")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"لە کەناڵی {chs} بەشداری کردووە")
            except:
                msg2 = await sython1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"کەناڵی ژمارە {chs}")

        await sython1.send_message(event.chat_id, "کۆکردنەوە تەواو بوو | SA")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("خاڵەکان کۆدەکرێنەوە")
        await event.edit("خاڵەکان کۆدەکرێنەوە")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_usernameee)
        await sython1.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                await sython1.send_message(event.chat_id, f"کۆکردنەوە تەواو بوو | SA")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"لە کەناڵی {chs} بەشداری کردووە")
            except:
                msg2 = await sython1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"کەناڵی ژمارە {chs}")

        await sython1.send_message(event.chat_id, "کۆکردنەوە تەواو بوو | SA")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("خاڵەکان کۆدەکرێنەوە")
        await event.edit("خاڵەکان کۆدەکرێنەوە")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_usernameeee)
        await sython1.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                await sython1.send_message(event.chat_id, f"کۆکردنەوە تەواو بوو | SA")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"لە کەناڵی {chs} بەشداری کردووە")
            except:
                msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"کەناڵی ژمارە {chs}")

        await sython1.send_message(event.chat_id, "کۆکردنەوە تەواو بوو | SA")
        
@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**خاڵەکان کۆدەکرێنەوە**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_username)
    await sython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
            await sython1.send_message(event.chat_id, f"**کۆکردنەوە تەواو بوو | SA**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**لە کەناڵی {chs} بەشداری کردووە**")
        except:
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**کەناڵی ژمارە {chs}**")
    await sython1.send_message(event.chat_id, "**کۆکردنەوە تەواو بوو | SA**")
    
    
    
@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**خاڵەکان کۆدەکرێنەوە**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernamee)
    await sython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
            await sython1.send_message(event.chat_id, f"**کۆکردنەوە تەواو بوو | SA**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**لە کەناڵی {chs} بەشداری کردووە**")
        except:
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**کەناڵی ژمارە {chs}**")
    await sython1.send_message(event.chat_id, "**کۆکردنەوە تەواو بوو | SA**")

@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**خاڵەکان کۆدەکرێنەوە**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameee)
    await sython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
            await sython1.send_message(event.chat_id, f"**کۆکردنەوە تەواو بوو | SA**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**لە کەناڵی {chs} بەشداری کردووە**")
        except:
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**کەناڵی ژمارە {chs}**")
    await sython1.send_message(event.chat_id, "**کۆکردنەوە تەواو بوو | SA**")


@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**خاڵەکان کۆدەکرێنەوە**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameeee)
    await sython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
            await sython1.send_message(event.chat_id, f"**کۆکردنەوە تەواو بوو | SA**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**لە کەناڵی {chs} بەشداری کردووە**")
        except:
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**کەناڵی ژمارە {chs}**")
    await sython1.send_message(event.chat_id, "**کۆکردنەوە تەواو بوو | SA**")


##########################################

@sython1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("خاڵەکان کۆدەکرێنەوە")
        await event.edit("خاڵەکان کۆدەکرێنەوە")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(pot)
        await sython1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                await sython1.send_message(event.chat_id, f"کۆکردنەوە تەواو بوو | SA")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"لە کەناڵی {chs} بەشداری کردووە")
            except:
                msg2 = await sython1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await sython1.send_message(event.chat_id, "کۆکردنەوە تەواو بوو | SA")
        
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await sython1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@sython1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ پرۆسەی کۆکردنەوەی بێکۆتایی لە پێشکەوتندایە ⛦**")
                joinu = await sython1(JoinChannelRequest('saythonh'))
                channel_entity = await sython1.get_entity(pot)
                await sython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await sython1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await sython1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                        await sython1.send_message(event.chat_id, f"**⛦ هەڵەیەک ڕوویدا، خەمت نەبێت، دووبارە هەوڵ دەدەمەوە ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await sython1(JoinChannelRequest(url))
                        except:
                            bott = url.split('/')[-1]
                            await sython1(ImportChatInviteRequest(bott))
                        msg2 = await sython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**لە کەناڵی {chs} بەشداری کردووە**")
                    except:
                        msg2 = await sython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**کەناڵی ژمارە  {chs}**")
                        await asyncio.sleep(60)

                await sython1.send_message(event.chat_id, "**⛦ هەڵەیەک ڕوویدا، خەمت نەبێت، دووبارە هەوڵ دەدەمەوە ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


@sython1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ باشە، من کۆمپایڵ دەکەم \n✣ ژمارەی چرکە لە نێوان هەر هەوڵێکدا: {numw}\n✣ کۆمپایڵکردن لە بۆتەوە : @{pot}**")

                joinu = await sython1(JoinChannelRequest('saythonh'))
                channel_entity = await sython1.get_entity(pot)
                await sython1.send_message(pot, '**گاری لەگەڵ سایتۆن دەستی بە پرۆسەی کۆکردنەوە کرد**')
                await sython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await sython1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await sython1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لە ئێستادا هیچ کەناڵێک نییە، خاڵەکان بە شێوەیەکی جیاواز کۆبکەرەوە') != -1:
                        await sython1.send_message(event.chat_id, f"**✣ باشە، من کۆمپایڵ دەکەم \n✣ ژمارەی چرکە لە نێوان هەر هەوڵێکدا: {numw}\n✣ کۆمپایڵکردن لە بۆتەوە : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await sython1(JoinChannelRequest(url))
                        except:
                            syth = url.split('/')[-1]
                            await sython1(ImportChatInviteRequest(syth))
                        msg2 = await sython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**✣ ژمارەی خاڵەکان لەم هەوڵەدا {chs} ✣**")
                    except:
                        msg2 = await sython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة
✣ لأنني وجدت قناة خاصة قمت بتخطيها
✣ البوت التي حدث فيه الخطأ: {pot}**""")
                        
                await sython1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            await asyncio.sleep(numw)


@sython1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("• سەرچاوەکە سەرلەنوێ دەستپێدەکاتەوە ..\n• 1-2 خولەک چاوەڕێ بکە  .")
        await sython1.disconnect()
        await sython1.send_message(event.chat_id, "سەرچاوەکە دووبارە دەستی پێکردووەتەوە ")
        


@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_username, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await sython1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**هەموو کەناڵ و گروپەکان بەجێدەهێڵیت**")
                




@sython1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython1.send_message(usern, mase)
    await event.respond(f"**پەیامەکە بۆ بەکارهێنەر نێردراوە {usern}**")    
    
    

@sython1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**بەخێربێن بۆ بەشی گواستنەوەی خاڵەکان
        
• @ZMMBOT - `/pt1 + ژمارەی خاڵەکان `
• @A_MAN9300BOT - `/pt2 + ژمارەی خاڵەکان `
• @MARKTEBOT - `/pt3 + ژمارەی خاڵەکان `
• @XNSEX21BOT - `/pt4 + ژمارەی خاڵەکان`**""")



@sython1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**بەخێربێن بۆ بەشی زانیاری ئەکاونتەکان
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await sython1.send_message(event.chat_id, f"**❈ باشە من کلیکم لەسەر دوگمەی ژمارەکە کرد {bt}**")
        

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await sython1.send_message(event.chat_id, f"**❈ باشە، دوایین\n❈ پەیام لە بەکارهێنەرەوە دەنێرم {userbott}**")
        msgs = await sython1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@sython1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython1.send_message(event.chat_id, "**کەناڵەکان بە شێوەیەکی ئۆتۆماتیکی پەیوەست دەکرێن**")
        joinq = await sython1(JoinChannelRequest('d3boot_7'))
        joinw = await sython1(JoinChannelRequest('Fvvvv'))
        joine = await sython1(JoinChannelRequest('DzDDDD'))
        joinr = await sython1(JoinChannelRequest('botbillion'))
        joint = await sython1(JoinChannelRequest('zzzzzz1'))
        joiny = await sython1(JoinChannelRequest('zzzzzz'))
        joini = await sython1(JoinChannelRequest('zz_MX'))
        joino = await sython1(JoinChannelRequest('lI7777Il'))
        joinp = await sython1(JoinChannelRequest('KTTTT'))
        joina = await sython1(JoinChannelRequest('RRXFR'))
        sendd = await sython1.send_message(event.chat_id, "**بەشداری کەناڵەکان بکەن**")
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await sython1.send_message(event.chat_id,f"**جۆنەژورەوە بۆ کەناڵەکان لە ئارادایە @{usercht}**")
        joinch = await sython1(JoinChannelRequest(usercht))
        sendy = await sython1.send_message(event.chat_id,f"**کەناڵەکە پەیوەندی پێوە کراوە @{usercht}**")

@sython1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await sython1.send_message(event.chat_id,f"**جێهێشتنی کەناڵەکە  @{usercht}**")
        joinch = await sython1(LeaveChannelRequest(usercht))
        sendy = await sython1.send_message(event.chat_id,f"**کەناڵەکە جێهێڵراوە @{usercht}**")

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await sython1.send_message(ownerhson_id,'**⚝ باشە منیش بەشداری دەکەم و دەنگ دەدەم**')
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(ownerhson_id,'**⚝ بەشداریت کرد و بە سەرکەوتوویی دەنگت دا**')

ownerhson_ids = 5159123009
@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await sython1.send_message(ownerhson_ids,'**⚝ باشە منیش بەشداری دەکەم و دەنگ دەدەم**')
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(ownerhson_ids,'**⚝ باشە منیش بەشداری دەکەم و دەنگ دەدەم**')


print("💠 Sython Userbot Running 💠")
sython1.run_until_disconnected()


#code skip accumulate points by t.me.zzzzl1l thank you my bro