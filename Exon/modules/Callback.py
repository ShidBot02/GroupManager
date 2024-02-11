"""
MIT License

Copyright (c) 2022 ABISHNOI69

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi1m
#     UPDATE   :- Abishnoi_bots
#     GITHUB :- ABISHNOI69 ""

from pyrogram.types import CallbackQuery
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler

from Exon import BOT_NAME, OWNER_ID, SUPPORT_CHAT, OWNER_USERNAME
from Exon import Abishnoi as pbot
from Exon import dispatcher


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅᴀʏs"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@pbot.on_callback_query()
async def close(Client, cb: CallbackQuery):
    if cb.data == "close2":
        await cb.answer()
        await cb.message.delete()


# CALLBACKS


def ABG_about_callback(update, context):
    query = update.callback_query
    if query.data == "ABG_":
        query.message.edit_text(
            text=f"*🤖 {BOT_NAME} :*"
            "\n\n*I can restrict users, Greet users with customizable welcome message, Set a group's Ruels, Advance anti-flood system, Warn users until they reach max limits with each predefined actions such as ban, mute, kick etc., Note keeping sysytem, Blacklists, Even Predetermined replies on certain keywords, Check admins permissions before executing any command and more stuffs.\n\n👨‍💻 Modified by @Shidoteshika1*",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Admins", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="Notes", callback_data="ABG_notes"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Support", callback_data="ABG_support"
                        ),
                        InlineKeyboardButton(
                            text="Creadits", callback_data="ABG_credit"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="⬅️ Back", callback_data="start_back"
                        ),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_admin":
        query.message.edit_text(
            text=f"━━━━━━━ *MUSIC PANNEL* ━━━━━━━\n\n__*All Commands Only for Admins :*__\n\n*/pause* - Pause thcurrent ongoing stream.\n*/resume* - Resume the paused stream.\n*/skip* or */next* - Skip the current ongoing stream.\n*/end* or */stop* - End the current ongoing stream.\n\n*Commands to Autho/Unauth any Users :*\n• Authorized users can skip, pause, resume and end the stream without admin rights.\n\n*/auth* username or reply to users message.\n- ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n*/unauth* username or reply to users message.\n- ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.\n*/authusers* - Shows the list of authorized users of the group.\n\n*Commands to play Songs :*\n\n*/play* - (song name/yt url)\n- sᴛᴀʀᴛs ᴩʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴏɴ ᴠᴄ.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="⬅️ Back", callback_data="ABG_"),
                        InlineKeyboardButton(text="Help ⁉️", callback_data="help_back"),
                    ]
                ]
            ),
        )

    elif query.data == "ABG_notes":
        query.message.edit_text(
            text=f"<b><u>SETTING UP NOTES</u> :</b>\n\nYou can Save message/media/audio or anything as notes.\n\nTo get a note simple use # at the beginning of predetermined word.\n\nYou can also set buttons for notes and filtters (Refer help menu)\n\n**",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="⬅️ Back", callback_data="ABG_"),
                  InlineKeyboardButton(text="Help ⁉️", callback_data="help_back")]]
            ),
        )
    elif query.data == "ABG_support":
        query.message.edit_text(
            text=f"*🤖 {BOT_NAME} Support Chats :*"
            "\n\nJoin my support group for report a problem",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click here to Join Group", url="https://t.me/ChatBox480")
                    ],
                    [
                        InlineKeyboardButton(text="🤖 About", callback_data="ABG_"),
                        InlineKeyboardButton(text="⬅️ Back", callback_data="start_back"),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_credit":  # Credit  i hope edit nai hoga
        query.message.edit_text(
            text=f"━━━━━━━ *CREDIT* ━━━━━━━\n\nThis Powefull group managent Bots Orginial Source Code is Provided by [ROCKY CEO](https://t.me/about_jeol).\n\nAnd now it is modified by @Shidoteshika1.\n\n━━━━━━━ *CREDIT* ━━━━━━━",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🤖 About", callback_data="ABG_"),
                        InlineKeyboardButton(text="⬅️ Back", callback_data="start_back"),
                    ],
                ]
            ),
        )


def Source_about_callback(update, context):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_text(
            text=f"""
*ʜᴇʏ,
 ᴛʜɪs ɪs {BOT_NAME} ,
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.*

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ : [ᴛᴇʟᴇᴛʜᴏɴ](https://github.com/LonamiWebs/Telethon)
[ᴩʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
ᴀɴᴅ ᴜsɪɴɢ [sǫʟᴀʟᴄʜᴇᴍʏ](https://www.sqlalchemy.org) ᴀɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) ᴀs ᴅᴀᴛᴀʙᴀsᴇ.

*ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :* [{BOT_NAME}](https://github.com/itz-jeol/ROCKY)


ᴇxᴏɴ ʀᴏʙᴏᴛ ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ ᴍɪᴛ ʟɪᴄᴇɴsᴇ.
© 2022 - 2023 [sᴜᴘᴘᴏʀᴛ](https://t.me/{SUPPORT_CHAT}) ᴄʜᴀᴛ, ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🧑‍", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ꜱᴏᴜʀᴄᴇ",
                            url="https://github.com/itz-jeol/ROCKY",  # DON'T CHANGE
                        ),
                    ],
                ]
            ),
        )


about_callback_handler = CallbackQueryHandler(
    ABG_about_callback, pattern=r"ABG_", run_async=True
)

source_callback_handler = CallbackQueryHandler(
    Source_about_callback, pattern=r"source_", run_async=True
)


dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(source_callback_handler)
