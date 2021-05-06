from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Haii Guys, Apa Kabar Kamu??:)) {message.from_user.first_name}!</b>

Aku adalah Bot Musik Telegram, Apabila Ingin Menggunakan Aku Invite Aku Dan Assisten Aku Ya Biar Berjalan Dengan Lancar, Apabila Ada Kendala Tidak Tau Cara Pakainya Bisa PC OWNERNYA!:))
━━━━━━━━━━━━━━━━━━━━━━━━━
Bot : @officialheartbot - Asisten : @AsisstantOneHeart
        """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡ Owner Aku!", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "🍃 Channel Aku!", url="https://t.me/@chvirtual62"
                    ),
                    InlineKeyboardButton(
                        "❤️ Grup Aku!", url="https://t.me/remaja_virtual62") 
                  ],[
                    InlineKeyboardButton(
                        "👸 My Bot Help!", url="https://t.me/Asisstant_groupbot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**💕 Pemutar Musik Is The On!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌙 Group Support!", url="https://t.me/remaja_virtual62"
                    ),
                    InlineKeyboardButton(
                        "⚡ Owner Aku!", url="https://t.me/boyfriendnice"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🎧 Pemutar Musik Is The On!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ Onwer Aku!", url="https://t.me/boyfriendnice") 
                ],[
                    InlineKeyboardButton(
                        "🌙 Group Support!", url="https://t.me/remaja_virtual62"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦇 Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
