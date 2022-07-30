from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙᴏᴛ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣️", url="https://t.me/MyBotsupport"),
         InlineKeyboardButton(" ᴘʟᴀʏɪɴɢ ɢʀᴏᴜᴘ ", url="https://t.me/BATTLE_GROUP_OF_HEXA"),
        ],
    ]

    START = """
ʜI {},

Tʜɪs ɪs {},
sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ.ᴛʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ᴡɪᴛʜ ғᴜʟʟ ᴄᴏᴅɪɴɢ ᴀɴᴅ ʙʏ @pokemonmaster856.
    """
