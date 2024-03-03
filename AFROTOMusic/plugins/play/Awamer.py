import asyncio
import os
from pyrogram.types import CallbackQuery
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from AFROTOMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command("الاوامر")
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
      photo=f"https://telegra.ph/file/f90f490b19e32f201ba03.jpg",
        caption=f"""**- <b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» استخـدم الازرار بالاسفـل 𝄞\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="afropl"),
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="afroch"),  
                 ],[
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="afroad"), 
                 ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="afromot"), 
                InlineKeyboardButton(
                        "‹ اوامر التسليه ›", callback_data="hmd"), 
                 ],[       
                       
                    InlineKeyboardButton(
                        "•✯ ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛 ✯•", url=f"https://t.me/UI_VM"),
                ],

            ]

        ),

    )
    
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبـاً بك عـزيـزي 𝄞</b>\n<b>» استخـدم الازرار بالاسفـل\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="afropl"),
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="afroch"),  
                 ],[
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="afroad"), 
                 ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="afromot"), 
                InlineKeyboardButton(
                        "‹ اوامر التسليه ›", callback_data="hmd"), 
                 ],[       
                       
                    InlineKeyboardButton(
                        "✯ ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛 ✯", url=f"https://t.me/UI_VM"),
                ],

            ]

        ),

    )
    @app.on_callback_query(filters.regex("afromt") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبـاً بك عـزيـزي المطـور </b>\n\n<b>» استخـدم الازرار بالاسفـل 𝄞\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• التحـديث •", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "• الـرفــع •", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "• الـحظــر •", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "• الاشعــارات & المسـاعــد •", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
                ],
            ]
        ),
    
    
@app.on_callback_query(filters.regex("afropl"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**-  اوامر التشغيل اتبع مايلي
 — — — — — — — — — — 

◇︰ __تشغيل__ أو __شغل__ : لبدء تشغيل الاغاني .

◇︰ __بينج__ : لقياس سرعة النت في البوت .

◇︰أوامر القناة : __تشغيل__ + أسم الأغنية  .

◇︰ __كتم__ او __مؤقت__ : لكتم الأغنية الحالية .

◇︰ __كمل__ : لألغاء كتم الاغنية الحالية .

◇︰ __تخطي__ : لتخطي الأغنية الحالية .

◇︰ __ايقاف__ : لايقاف تشغيل الأغنية الحالية .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="zzzback"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("afroch"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**-<b>قائمــة اوامــر التشغيــل فـي القنــاة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل مباشـر</b>
<b>- ارسـل (/channelplay او ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الاوامــر بالاسفـل لـ التشغيـل</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

فيديو + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

ايقاف / انهاء / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / استئناف
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عـدد الثـوانـي
<b>- لـ تقديـم الاغنيـه لـ الامـام</b>
/seekback + عـدد الثـوانـي
<b>- لـ إرجـاع الاغنيـه لـ الخـلف</b>
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="zzzback"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("afroad"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**● <b>قائمــة اوامــر الادمــن :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

الاعدادات
<b>- لـ عـرض إعـدادات اوضـاع التشغيـل</b>

ايقاف / انهاء / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / كملي
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>

الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>

بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>

رفع ادمن/تنزيل ادمن
<b>- لـ رفـع/تنزيـل ادمـن فـي البـوت</b>

الادمنيه
<b>- لـ عـرض قائمـة ادمنيـة البـوت</b>-**"",
        
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="zzzback"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("hmd"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**-  اوامر التسليه
 — — — — — — — — — — 
كت
تويت
شعر
قول
صراحه 
انصحني

- ( all ) لعمل تاك جماعي في المجموعه

— — — — — — — — — — — — — —**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="zzzback"), 
                    
                ]
            ]
        )
    )
    
  @app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر التحـديثـات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجلات
<b>- لـ جلب سجـلات البـوت 📋</b>

تحديث
<b>- لـ تحديـث البــوت</b>

اعاده تشغيل
<b>- لـ اعـادة تشغيـل البــوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرفــع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

رفع مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي ميـوزك البـوت</b>

المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الحظــر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

بلوك/الغاء بلوك/المبلكين
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت</b>

احظره عام/الغاء حظره عام
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت عـام</b>

المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>

حظر مجموعة/سماح
<b>- لـ حظـر/الغـاء حظـر مجموعـة من استخـدام ميـوزك البـوت</b>

المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- لـ تفعيـل/تعطيـل اشعـارات مجموعـة سجـل البــوت</b>

المغادره التلقائيه تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل المغـادره التلقائيـه لـ الحسـاب المسـاعـد مـن المجمـوعـات عنـد عـدم استـخـدام الميـوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )
