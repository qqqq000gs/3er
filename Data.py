from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 ¦ مرحبـاً بـك عزيـزي  {}
✠━━━━━━━━❖━━━━━━━━━✠
 📮 ¦ في بوت 📬 {} 
━━━━━━━━━━━━━━━━━━━
🕹 ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @T_T_X_N
✠━━━━━━━━❖━━━━━━━━━✠

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [InlineKeyboardButton(text="⚜️¦ رجــوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [
            InlineKeyboardButton("⚜️¦ كيف تستخدمني", callback_data="help"),
            InlineKeyboardButton("⚜️¦ حــول", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **📬 ¦ كـيف تستخـدمني** ✨

× /about - حول البوت
× /help - لتسوي روحك كلشي متعرف
× /start - حتى تشغل البوت
× /generate - حتى تبدا بأستخراج البوت
× /cancel - لألغاء الاستخراج
× /restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**⚜️¦حـول البـوت** 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس ال ميم 

- قنـاة السـورس : @N_J_9

استخدم البوت : 

»[Pyrogram](docs.pyrogram.org)
🕹
»[Python](www.python.org)

لغة البوت : [بايثون](www.python.org)

⚜️¦ المطور  : [ تم كتابه هاذا الملف بواسطه ال ميم ](https://t.me/N_J_9)
    """
