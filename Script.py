class script(object):
    START_TXT = """<b>Hello {},
I'm A Telegram 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗋𝖾 𝖿𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝖾𝖽 AutoFilter Bot.Its Easy To Use Me ):\nJust Add Me To Your Group As Admin,Hit The /help For More Info</b>"""
    HELP_TXT = """<b>𝖧𝖾𝗒 {} 𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:
/start - 𝖼𝗁𝖾𝖼𝗄 𝗐𝗁𝖾𝗍𝗁𝖾𝗋 𝗂𝗆 𝗈𝗇𝗅𝗂𝗇𝖾 
/help - 𝗀𝖾𝗍 𝗍𝗁𝗂𝗌 𝗁𝖾𝗅𝗉 𝗆𝖾𝗌𝗌𝖺𝗀𝖾
/about - 𝖺𝖻𝗈𝗎𝗍 𝗆𝖾</b>"""
    ABOUT_TXT = """
<b>➥  My Name</b> : <b><i><a href="https://t.me/MC_MovieBot">Mᴏᴠɪᴇ Bᴏᴛ 😎</a></i></b>
<b>➥  Owner</b> : <b><i><a href="https://t.me/TomHiiddleston">Tᴏᴍ Hɪᴅᴅʟᴇsᴛᴏɴ</a></i></b>
<b>➥ Credits</b> : <code>Everyone in this journey</code>
<b>➥ Data base</b> : <b><a href="https://www.mongodb.com/">MongoDB</a></b>
<b>➥ Language</b> : <code>Python3</code>
<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>
<b>➥ Server</b> : <code>AWS</code>
<b>➥ Build Stats</b> : <code>V6.0 [BETA]</code>

©️ MᴀɪɴᴛᴀɪɴᴇD Bʏ  <a href=https://t.me/MovieClubOfficiall>Mᴏᴠɪᴇ Cʟᴜʙ</a>"""
    SOURCE_TXT = """
<code>All the files in this bot are freely available on the internet or posted by somebody else.This bot is indexing files which are already uploaded on Telegram for easy of searching, We respect all the copyright laws and works in compliance with DMCA and EUCD. If anything is against law please contact us so that it can be removed asap.</code>"""
    FILE_TXT = """Help: <b><u>File Store</u></b>
<b>By Using This Module You can store files in My database and I will You A Permanent link To access The saved Files.If You want to add files from a Public channel send the file link only or You want to store files from a Private channel you must make me admin on their to access files files (only media messages  can be stored).
⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /plink - <b>𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝖽𝗂𝖺 𝗍𝗈 𝗀𝖾𝗍 𝗅𝗂𝗇𝗄.</b>
• /pbatch - <b>𝖴𝗌𝖾 𝗒𝗈𝗎𝗋 𝗆e𝖽𝗂𝖺 𝗅𝗂𝗇𝗄 𝗐𝗂𝗍𝗁 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽.</b>
• /batch - <b>To Create Link For Multiple Post.</b>
❗️𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/batch https://t.me/MovieClubOfficiall/7 https://t.me/MovieClubOfficiall/10</code>"""
    WHOIS_TXT ="""Help: <b><u>WHO IS</u></b>
<b>By Using This Module You Can Get A User Details
⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
•/whois : Get a users full details"""
    FUN_TXT ="""Help: <b><u>Fun</u></b> 
    
<b>🎲 NOTHING MUCH JUST SOME FUN THINGS
⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 
𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUELFILTER_TXT = """Help: <b><u>Manual Filters</u></b>
<b>Filter is the feature were users can set automated replies for a particular keyword and 𝖭𝖺𝗍𝗁𝖺𝗅𝗂𝖺  will respond whenever a keyword is found the message</b>
<b>NOTE:</b>
1. 𝖭𝖺𝗍𝗁𝖺𝗅𝗂𝖺 should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """Help: <b><u>Song Download</u></b>
<b>By Using This Module You Can Download Your Favorite Tunes, For Those Who Love Music.</b>
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /song [Correct Song Name] - To Download Music From YouTube
<b>Note</b>
• Can Be Used By Everyone
• Works in bot pm Also"""
    PIN_TXT ="""Help: <b><u>PIN</u></b>
<b>By Using This Module Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
◉ /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
◉ /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b><u>Paste</u></b>
<b>By Using This Module, You can Paste some texts or documents on a website!</b>
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /paste [text] - paste the given text on Pasty
<b>NOTE:</b>
• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """Help: <b><u>Text To Speech</u></b>
<b>By Using This Module, You Can Translate text to speech</b>
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /tts <text> : Convert Your text to speech
<b>NOTE:</b>
• 𝖭𝖺𝗍𝗁𝖺𝗅𝗂𝖺 should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""Help: <b><u>Torrent Search</u></b>
<b>By Using This Module, You Can Get Your Torrent Link From Various Resource</b> 
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>:
• /torrent or /tor : Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
• 𝖭𝖺𝗍𝗁𝖺𝗅𝗂𝖺 should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-ᗩᒍᗩ᙭  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᗩᒍᗩ᙭ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MWUpdatez)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """**𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙾𝙽/𝙾𝙵𝙵 𝙼𝙾𝙳𝚄𝙻𝙴..

𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙰𝙽𝙳 𝚂𝙰𝚅𝙴  𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲𝙰𝙻𝙻𝚈 𝙵𝚁𝙾𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙶𝚁𝙾𝚄𝙿. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚃𝙾 𝙾𝙽 𝙰𝙽𝙳 𝙾𝙵𝙵 𝚃𝙷𝙴 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿../

𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 :-
›› /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂..
›› /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂..
›› /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁. 
›› /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.

𝙲𝚁𝙴𝙳𝙸𝚃𝚂 :- <a href=https://t.me/OpusTechz>𝙾𝙿𝚄𝚂-𝚃𝙴𝙲𝙷𝚉</a>**"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ᗩᒍᗩ᙭ 

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>᚛› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>
<b>᚛› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """➤ 𝐇𝐞𝐥𝐩: Rᴇᴘᴏʀᴛ ⚠️

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚛𝚎𝚙𝚘𝚛𝚝 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚛 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚏 𝚝𝚑𝚎 𝚛𝚎𝚜𝚙𝚎𝚌𝚝𝚒𝚟𝚎 𝚐𝚛𝚘𝚞𝚙. 𝙳𝚘𝚗'𝚝 𝚖𝚒𝚜𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽

𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/kB9TkCs8cX0</code>"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/kB9TkCs8cX0)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/kB9TkCs8cX0</code>
<code>/video https://youtu.be/kB9TkCs8cX0</code>"""

    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨

𝖬𝖺𝖽𝖾 𝖻𝗒 <a href=https://t.me/MWUpdatez>𝙼𝚆-𝚄𝙿𝙳𝙰𝚃𝙴𝚉</a>"""

    STICKER_TXT = """𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/UyzJ9KEoU0w</code>"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄

𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
