import re
from pyrogram import filters, Client
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from info import ADMINS, LOG_CHANNEL, FILE_STORE_CHANNEL, PUBLIC_FILE_STORE
from database.ia_filterdb import unpack_new_file_id
from utils import temp
import re
import os
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False

@Client.on_message(filters.command(['link', 'plink']) & filters.create(allowed))
async def gen_link_s(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('**𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖮𝖱 𝖠 𝖥𝗂𝗅𝖾. 𝖨 𝖶𝗂𝗅𝗅 𝖦𝗂𝗏𝖾 𝖸𝗈𝗎 𝖠 𝖲𝗁𝖺𝗋𝖺𝖻𝗅𝖾 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖫𝗂𝗇𝗄**')
    file_type = replied.media
    if file_type not in ["video", 'audio', 'document']:
        return await message.reply("𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝖬𝖾𝖽𝗂𝖺")
    if message.has_protected_content and message.chat.id not in ADMINS:
        return await message.reply("𝖳𝗁𝗂𝗌 𝖨𝗌 𝖭𝗈𝗍 𝖥𝗈𝗋 𝖸𝗈𝗎 😒")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type)).file_id)
    string = 'filep_' if message.text.lower().strip() == "/plink" else 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    await message.reply(f"<b>𝖧𝖾𝗋𝖾 𝖨𝗌 𝖸𝗈𝗎𝗋 𝖫𝗂𝗇𝗄:</b>\n\nhttps://t.me/{temp.U_NAME}?start={outstr}")
    
    
@Client.on_message(filters.command(['batch', 'pbatch']) & filters.create(allowed))
async def gen_link_batch(bot, message):
    if " " not in message.text:
        return await message.reply("<b>𝖯𝗅𝖾𝖺𝗌𝖾 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖳𝗁𝖾 𝖥𝗋𝗂𝗌𝗍 𝖯𝗈𝗌𝗍 𝖥𝗋𝗈𝗆 𝖳𝗁𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 (𝖶𝗁𝖾𝗋𝖾 𝖨 𝖠𝗆 𝖠 𝖠𝖽𝗆𝗂𝗇)\n\n𝖴𝗌𝖾 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖥𝗈𝗋𝗆𝖺𝗍.</b>\n\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 : <code>/batch https://t.me/MovieClubOfficiall/7 https://t.me/MovieClubOfficiall/10</code>.")
    links = message.text.strip().split(" ")
    if len(links) != 3:
        return await message.reply("<b>𝖯𝗅𝖾𝖺𝗌𝖾 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖳𝗁𝖾 𝖥𝗋𝗂𝗌𝗍 𝖯𝗈𝗌𝗍 𝖥𝗋𝗈𝗆 𝖳𝗁𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 (𝖶𝗁𝖾𝗋𝖾 𝖨 𝖠𝗆 𝖠 𝖠𝖽𝗆𝗂𝗇) 𝖴𝗌𝖾 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖥𝗈𝗋𝗆𝖺𝗍.</b>\n\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 : <code>/batch https://t.me/MovieClubOfficiall/7 https://t.me/MovieClubOfficiall/10</code>.")
    cmd, first, last = links
    regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
    match = regex.match(first)
    if not match:
        return await message.reply('Invalid link')
    f_chat_id = match.group(4)
    f_msg_id = int(match.group(5))
    if f_chat_id.isnumeric():
        f_chat_id  = int(("-100" + f_chat_id))

    match = regex.match(last)
    if not match:
        return await message.reply('Invalid link')
    l_chat_id = match.group(4)
    l_msg_id = int(match.group(5))
    if l_chat_id.isnumeric():
        l_chat_id  = int(("-100" + l_chat_id))

    if f_chat_id != l_chat_id:
        return await message.reply("𝖢𝗁𝖺𝗍 𝖨𝖣 𝖭𝗈𝗍 𝖬𝖺𝗍𝖼𝗁𝖾𝖽 🧐")
    try:
        chat_id = (await bot.get_chat(f_chat_id)).id
    except ChannelInvalid:
        return await message.reply('𝖳𝗁𝗂𝗌 𝖬𝖺𝗒 𝖡𝖾 𝖠 𝖯𝗋𝗂𝗏𝖺𝗍𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖮𝖱 𝖦𝗋𝗈𝗎𝗉. 𝖬𝖺𝗄𝖾 𝖬𝖾 𝖠𝗇 𝖠𝖽𝗆𝗂𝗇 𝖮𝗏𝖾𝗋 𝖳𝗁𝖾𝗋𝖾 𝖳𝗈 𝖨𝗇𝖽𝖾𝗑 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 📁.')
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply('𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖫𝗂𝗇𝗄 𝖲𝗉𝖾𝖼𝗂𝖿𝗂𝖾𝖽 🤕.')
    except Exception as e:
        return await message.reply(f'Errors - {e}')

    sts = await message.reply("𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖫𝗂𝗇𝗄 𝖥𝗈𝗋 𝖸𝗈𝗎𝗋 𝖬𝖾𝗌𝗌𝖺𝗀𝖾.\n𝖳𝗁𝗂𝗌 𝖬𝖺𝗒𝖡𝖾 𝖳𝖺𝗄𝖾 𝖳𝗂𝗆𝖾 𝖣𝖾𝗉𝖾𝗇𝖽𝗂𝗇𝗀 𝖴𝗉𝗈𝗇 𝖳𝗁𝖾 𝖭𝗎𝗆𝖻𝖾𝗋 𝖮𝖿 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌")
    if chat_id in FILE_STORE_CHANNEL:
        string = f"{f_msg_id}_{l_msg_id}_{chat_id}_{cmd.lower().strip()}"
        b_64 = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
        return await sts.edit(f"<b>𝖧𝖾𝗋𝖾 𝖨𝗌 𝖸𝗈𝗎𝗋 𝖫𝗂𝗇𝗄:</b>\n\nhttps://t.me/{temp.U_NAME}?start=DSTORE-{b_64}")

    FRMT = "<b>╭━━━━━━━━━━━━━━━➣\n┣⪼𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝖫𝗂𝗇𝗄 ⏳\n┣⪼𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 📜: `{total}` \n┣⪼𝖣𝗈𝗇𝖾 🗳️: `{current}`\n┣⪼𝖱𝖾𝗆𝖺𝗂𝗇𝗂𝗇𝗀 📤: `{rem}`\n┣⪼𝖲𝗍𝖺𝗍𝗎𝗌 💬: `{sts}`\n╰━━━━━━━━━━━━━━━➣</b>"

    outlist = []

    # file store without db channel
    og_msg = 0
    tot = 0
    async for msg in bot.iter_messages(f_chat_id, l_msg_id, f_msg_id):
        tot += 1
        if msg.empty or msg.service:
            continue
        if not msg.media:
            # only media messages supported.
            continue
        try:
            file_type = msg.media
            file = getattr(msg, file_type)
            caption = getattr(msg, 'caption', '')
            if caption:
                caption = caption.html
            if file:
                file = {
                    "file_id": file.file_id,
                    "caption": caption,
                    "title": getattr(file, "file_name", ""),
                    "size": file.file_size,
                    "protect": cmd.lower().strip() == "/pbatch",
                }

                og_msg +=1
                outlist.append(file)
        except:
            pass
        if not og_msg % 20:
            try:
                await sts.edit(FRMT.format(total=l_msg_id-f_msg_id, current=tot, rem=((l_msg_id-f_msg_id) - tot), sts="Saving Messages"))
            except:
                pass
    with open(f"batchmode_{message.from_user.id}.json", "w+") as out:
        json.dump(outlist, out)
    post = await bot.send_document(LOG_CHANNEL, f"batchmode_{message.from_user.id}.json", file_name="Batch.json", caption="👩🏻‍💻 File Store Logs 👩🏻‍💻")
    os.remove(f"batchmode_{message.from_user.id}.json")
    file_id, ref = unpack_new_file_id(post.document.file_id)
    await sts.edit(f"<b>𝖧𝖾𝗋𝖾 𝖨𝗌 𝖸𝗈𝗎𝗋 𝖫𝗂𝗇𝗄\n𝖢𝗈𝗇𝗍𝖺𝗂𝗇𝗌</b><b> `{og_msg}` 𝖥𝗂𝗅𝖾𝗌.</b>\n\n<b>›› https://t.me/{temp.U_NAME}?start=BATCH-{file_id}</b>")
