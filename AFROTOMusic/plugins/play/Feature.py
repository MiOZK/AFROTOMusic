import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

@app.on_message(
    filters.command(["مميزات","مميزات الزعيم"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس  الزعيم ميوزك\n
⩹━★⊷⌯⌞ ᯓ𖡡🇾🇪-•┋الـ||ـزﻋيـم ┋⌝⌯⊶★━⩺

★قايمه مميزات سورس الزعيم

★ميزه ⦂ تبيه بفتح+قفل الكول
★ميزه ⦂ ترحيب دخول و خروج الاعضاء 
★ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
★ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
★ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
★ميزه ⦂ تلغراف ميديا بردعالصوره
★ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
★ميزه ⦂ الصوتيه..ف كول
★ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالكول
★ميزه ⦂ بث مباشر للقنوات 
★ميزه ⦂ اسمي بيجب الاسم
★ميزه ⦂ سورس بيجب السورس
★ميزه ⦂ حظر+كتم ميوزك
★ميزه ⦂ مبرمج
★ميزه ⦂ الاحصائيات
★ميزه ⦂ الاذكار
★ميزه ⦂ دعوه في كول
★ميزه ⦂  دعوه فالخاص بتاع البوت
★ميزه ⦂ تنبيه..بانضمام بوت في الجروبات
★ميزه ⦂ بايو
★ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
★ميزه ⦂ اسال/اصراحه
★ميزه ⦂ نكت
★ميزه ⦂ ذكاء اصتناعي 
★ميزه ⦂ مميزات. بيجبلك مميزات موجوده فسورس 
★ميزه ⦂ رفع و تنزيل مطور 
★ميزه ⦂ افلام
★ميزه ⦂ مكالمات النشطه+مجموعات البوت شغال فيها
★ميزه ⦂ اساله دينيه
★ميزه ⦂ مين فالكول+بتعرف مين فكول و عددهم
★ميزه ⦂ انا فين+بتجلك جروب
★ميزه ⦂ الرابط+رابط مجموعه
★ميزه ⦂ فنان+اكتب اسم فنان و هتجبلك اغانيه
★ميزه ⦂ اصدار+حول

⩹━★⊷⌯⌞ ᯓ𖡡🇾🇪-•┋الـ||ـزﻋيـم ┋ 𖠛 ⌝⌯⊶★━⩺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "# 𝗠𝗜𝗨𝗭𝗜𝗞 𝗔𝗟𝗭𝗔𝗘𝗜𝗠 𖠛⌝⚡", url=f"https://t.me/VVV5P"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

