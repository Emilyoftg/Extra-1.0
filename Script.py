class script(object):
    START_TXT = """<b>𝖧𝖾𝗅𝗅𝗈 {},
𝗅'm 𝖠 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝗂𝗆𝗉𝗅𝖾 𝖯𝗋𝖾 𝖥𝗎𝖼𝗍𝗂𝗈𝗇𝖾𝖽 𝖠𝗎𝗍𝗈𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍.𝖨𝗍𝗌 𝖤𝖺𝗌𝗒 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾 ):\n𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 Admin,𝖧𝗂𝗍 𝖳𝗁𝖾 /help 𝖥𝗈𝗋 𝖬𝗈𝗋𝖾 𝖨𝗇𝖿𝗈</b>"""
    HELP_TXT = """<b>𝖧𝖾𝗒 {} 𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:
/start - 𝖼𝗁𝖾𝖼𝗄 𝗐𝗁𝖾𝗍𝗁𝖾𝗋 𝗂𝗆 𝗈𝗇𝗅𝗂𝗇𝖾 
/help - 𝗀𝖾𝗍 𝗍𝗁𝗂𝗌 𝗁𝖾𝗅𝗉 𝗆𝖾𝗌𝗌𝖺𝗀𝖾
/about - 𝖺𝖻𝗈𝗎𝗍 𝗆𝖾</b>"""
    ABOUT_TXT = """
<b>➥  𝖬𝗒 𝖭𝖺𝗆𝖾</b> : <b><i><a href="https://t.me/MC_MovieBot">Mᴏᴠɪᴇ Bᴏᴛ 😎</a></i></b>
<b>➥  𝖮𝗐𝗇𝖾𝗋</b> : <b><i><a href="https://t.me/TomHiiddleston">Tᴏᴍ Hɪᴅᴅʟᴇsᴛᴏɴ</a></i></b>
<b>➥ 𝖢𝗋𝖾𝖽𝗂𝗍𝗌</b> : <code>Everyone in this journey</code>
<b>➥ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾</b> : <b><a href="https://www.mongodb.com/">MongoDB</a></b>
<b>➥ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾</b> : <code>Python3</code>
<b>➥ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>
<b>➥ 𝖲𝖾𝗋𝗏𝖾𝗋</b> : <code>AWS</code>
<b>➥ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗌</b> : <code>V6.0 [BETA]</code>

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
𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗋𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 
𝖭𝖮𝖳𝖤: 
𝟣. 𝖻𝗈𝗍 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾 𝗂𝗇 𝗈𝗋𝖽𝖾𝗋 𝗍𝗈 𝗋𝖾𝗉𝗅𝗒 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟤. 𝗈𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟥. 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖽𝗈𝖾𝗌 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖺𝗋𝗄𝖽𝗈𝗐𝗇𝗌, 𝗆𝖾𝖽𝗂𝖺𝗌 𝖺𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌. 
𝟦. 𝖺𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝖺𝗋𝖾 𝖺𝗅𝗌𝗈 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝗐𝗂𝗍𝗁 𝖺 𝗅𝗂𝗆𝗂𝗍 𝗈𝖿 𝟨𝟦 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌. 
<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
/filter  𝗈𝗋 /add - 𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋
/filters 𝗈𝗋 /viewfilters - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍 
/stop 𝗈𝗋 /del - 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋 (𝗌𝖾𝗉𝖺𝗋𝖺𝗍𝖾 𝗄𝖾𝗒𝗐𝗈𝗋𝖽𝗌 𝗐𝗂𝗍𝗁 𝗌𝗉𝖺𝖼𝖾𝗌 𝖿𝗈𝗋 𝖽𝖾𝗅𝖾𝗍𝗂𝗇𝗀 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖺𝗍 𝖺 𝗍𝗂𝗆𝖾) 
/stopall 𝗈𝗋 /delall - 𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍 (𝖼𝗁𝖺𝗍 𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒)"""
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
    TELE_TXT = """HELP: <b><u>Telegraph</u></b>
<b> By Using This Module, You can convert gif, image or video into telegra.ph links</b>
</b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /telegraph - Send me Picture or Video Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
    JSON_TXT ="""Help: <b><u>JSON</u></b>

<b>By Using This Module, Bot returns json for all replied messages with /json</b>

</b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• /json - To Get Json Of Replied Messages
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
    PURGE_TXT = """Help: <b><u>Purge</u></b>
    
<b>By Using This Module, You Can Delete Messages From Groups!</b>
    
 </b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message
<b>NOTE:</b>
• This Command Is Available in goups only
• This Command Can be used by Admins only"""
    BUTTON_TXT = """Help: <b><u>Buttons</u></b>

<b>Nathaliya 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌, 𝗇𝗈𝗐 𝗅𝖾𝗍𝗌 𝗌𝖾𝖾 𝗁𝗈𝗐 𝗍𝗈 𝗂𝗆𝗉𝗅𝖾𝗆𝖾𝗇𝗍 𝗂𝗍.</b> 

<b>NOTE:</b>
𝟣. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒. 
𝟤. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾. 
𝟥. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝖿𝗈𝗋𝗆𝖺𝗍𝗍𝖾𝖽 𝖺𝗌 𝖻𝖾𝗅𝗈𝗐 𝗈𝗋 𝖾𝗅𝗌𝖾 𝗋𝖾𝗌𝗎𝗅𝗍 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗆𝖺𝗅𝖿𝗈𝗋𝗆𝖾𝖽. 

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieClubOfficiall)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:Hello, This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b><u>AutoFilter</u></b>

<b>𝖭𝖮𝖳𝖤:</b> 
𝟣. 𝖬𝖺𝗄𝖾 𝗆𝖾 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗂𝖿 𝗂𝗍'𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾. 
𝟤. 𝗆𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖽𝗈𝖾𝗌 𝗇𝗈𝗍 𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖼𝖺𝗆 𝗋𝗂𝗉, 𝗉𝗈𝗋𝗇 𝖺𝗇𝖽 𝖿𝖺𝗄𝖾 𝖿𝗂𝗅𝖾𝗌. 
𝟥. 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝗍𝗁𝖾 𝗅𝖺𝗌𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗆𝖾 𝗐𝗂𝗍𝗁 𝗊𝗎𝗈𝗍𝖾𝗌.  𝖨'𝗅𝗅 𝖺𝖽𝖽 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝖺𝗍 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗆𝗒 𝖽𝖻.

</b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
›› /autofilter on - 𝖤𝗇𝖺𝖻𝗅𝖾𝗌 𝖠𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖨𝗇 𝖳𝗁𝖾 𝖣𝖾𝗌𝗂𝗋𝖾𝖽 𝖢𝗁𝖺𝗍
›› /autofilter off - 𝖣𝗂𝗌𝖺𝖻𝗅𝖾𝗌 𝖠𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖨𝗇 𝖳𝗁𝖾 𝖣𝖾𝗌𝗂𝗋𝖾𝖽 𝖢𝗁𝖺𝗍
›› /set_template - 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖨𝖬𝖣𝖡 𝖳𝖾𝗆𝗉𝗅𝖺𝗍𝖾 𝖥𝗈𝗋 𝖠𝗎𝗍𝗈𝖥𝗂𝗅𝗍𝖾𝗋 
›› /get_template - 𝖦𝖾𝗍 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖨𝖬𝖡𝖣 𝖳𝖾𝗆𝗉𝗅𝖺𝗍𝖾 𝖮𝖿 𝖠𝗎𝗍𝗈𝖥𝗂𝗅𝗍𝖾𝗋."""
    CONNECTION_TXT = """Help: <b><u>Connections</u></b>

𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖻𝗈𝗍 𝗍𝗈 𝖯𝖬 𝗐𝗁𝗂𝖼𝗁 𝗅𝖾𝗍 𝗐𝗂𝗅𝗅 𝗒𝗈𝗎 𝗍𝗈 𝖾𝗑𝖾𝖼𝗎𝗍𝖾 𝖻𝗈𝗍𝗁 𝗇𝗈𝗋𝗆𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝗌𝗈𝗆𝖾 𝗈𝗍𝗁𝖾𝗋 𝗌𝖾𝗇𝗌𝗂𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗋𝗂𝗀𝗁𝗍 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖯𝖬 𝗍𝗁𝖺𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝖿𝗅𝖾𝖼𝗍 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉 𝗐𝗁𝗂𝖼𝗁 𝗁𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋 𝖺𝖽𝖽𝗂𝗍𝗂𝗈𝗇𝗌 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗌𝗍𝗎𝖿𝖿𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖺𝗇𝖽 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝗉𝗋𝖾𝗏𝖾𝗇𝗍 𝖿𝗅𝗈𝗈𝖽𝗂𝗇𝗀. 
<b>𝖭𝖮𝖳𝖤:</b> 
𝟣. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇. 
𝟤. 𝖨𝗇 𝖺 𝖼𝗁𝖺𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝗂𝗆𝗉𝗅𝗒 𝗎𝗌𝖾 𝗍𝗁𝖾 /connect 𝖿𝗈𝗋 𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇  
𝟥. 𝖨𝗇 𝖯𝖬 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝖼𝗁𝖺𝗍 𝗂𝖽 𝗋𝗂𝗀𝗁𝗍 𝖺𝖿𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽. 
</b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
/connect - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬 
/disconnect  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍 
/connections - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌"""
    EXTRAMOD_TXT = """Help: <b><u>Extra Modules</u></b>

<b>NOTE:</b>
these are the extra features of 𝖭𝖺𝗍𝗁𝖺𝗅𝗂𝖺

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
    STATUS_TXT = """<b>• Saved Files:</b> <code>{}</code>
<b>• Users:</b> <code>{}</code>
<b>• Groups:</b> <code>{}</code>
<b>• DB Usage:</b> <code>{}</code> MiB"""
    LOG_TEXT_G  = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› Gʀᴏᴜᴘ ⪼ {}(<code>{}</code>)</b>
<b>᚛› Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs ⪼ <code>{}</code></b>
<b>᚛› Aᴅᴅᴇᴅ Bʏ ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖱𝖾𝗉𝗈𝗋𝗍</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖱𝖾𝗉𝗈𝗋𝗍 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖮𝖱 𝖠 𝖲𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖴𝗌𝖾𝗋𝗌 𝖳𝗈 𝖳𝗁𝖾 𝖠𝖽𝗆𝗂𝗇𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖱𝖾𝗌𝗉𝖾𝖼𝗍𝗂𝗏𝖾 𝖦𝗋𝗈𝗎𝗉.</b>

 </b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b> 
» /report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾).

<b>NOTE:</b>
• This Command Is Available in goups
• This Command Can be used by everyone"""

    CORONA_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖢𝗈𝗏𝗂𝖽 𝖵𝗂𝗋𝗎𝗌</u></b>

<𝖻>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖣𝖺𝗂𝗅𝗒 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖠𝖻𝗈𝗎𝗍 𝖢𝗈𝗏𝗂𝖽 𝖵𝗂𝗋𝗎𝗌 </b>

 <b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b> 
• /covid - 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 𝖭𝖺𝗆𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖢𝗈𝗏𝗂𝖽 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
›› Exᴀᴍᴘʟᴇ :
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>

<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    URLSHORT_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖴𝗋𝗅 𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋</u></b>

<𝖻>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖲𝗁𝗈𝗋𝗍𝖾𝗇 𝖸𝗈𝗎𝗋 𝖫𝗈𝗇𝗀𝖾𝗋 𝖴𝗋𝗅 𝖳𝗈 𝖲𝗁𝗈𝗋𝗍 𝖴𝗋𝗅</b>

<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b> 

➪ /short: 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝖽 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖫𝗂𝗇𝗄 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗁𝗈𝗋𝗍𝖾𝗇𝖾𝖽 𝖫𝗂𝗇𝗄

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/QWiCboxG-Lo</code>
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""


    VIDEO_TXT ="""𝖧𝖾𝗅𝗉: <b><u>𝖵𝖾𝖽𝗂𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝖾𝗋</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖠𝗇𝗒 𝖵𝖾𝖽𝗂𝗈 𝖥𝗋𝗈𝗆 𝖸𝗈𝗎𝖳𝗎𝖻𝖾</b>

<b>⪼ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾</b>
• 𝖳𝗒𝗉𝖾 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/QWiCboxG-Lo)
• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/mp4 https://youtu.be/QWiCboxG-Lo</code>
<code>/video https://youtu.be/QWiCboxG-Lo</code>
<b>NOTE:</b>
• This Command Is Available in pms
• This Command Can be used by everyone"""

    ZOMBIES_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖹𝗈𝗆𝖻𝗂𝖾𝗌</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖪𝗂𝖼𝗄 𝖨𝗇𝖺𝖼𝗍𝗂𝗏𝖾 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 𝖥𝗋𝗈𝗆 𝖦𝗋𝗈𝗎𝗉. 𝖠𝖽𝖽 𝖬𝖾 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇 𝖶𝗂𝗍𝗁 𝖡𝖺𝗇 𝖴𝗌𝖾𝗋𝗌 𝖯𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇 𝖨𝗇 𝖦𝗋𝗈𝗎𝗉.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts.
<b>NOTE:</b>
• This Command Is Available in goups
• This Command Can be used by 𝖺𝖽𝗆𝗂𝗇𝗌"""

    IMAGE_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖨𝗆𝖺𝗀𝖾 𝖤𝖽𝗂𝗍𝗈𝗋</u></b>
<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎l𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖤𝖽𝗂𝗍 𝖨𝗆𝖺𝗀𝖾𝗌 𝖵𝖾𝗋𝗒 𝖤𝖺𝗌𝗂𝗅𝗒</b> 

<b>Commands and Usage:</b>
» 𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖳𝗁𝖾 𝖨𝗆𝖺𝗀𝖾 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 & 𝖶𝖺𝗂𝗍

<b>NOTE:</b>
• This Command Is Available in pms
• This Command Can be used by everyone"""

    STICKER_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖣</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 Get 𝖠𝗇𝗒 Sticker ID</b>
 
<b>Commands and Usage:</b>
 
◉ /stickerid - 𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠𝗇𝗒 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖶𝗁𝗂𝖼𝗁 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖳𝗈 𝖦𝖾𝗍 𝖨𝖣
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""


    YTTHUMB_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖸𝗈𝗎𝖳𝗎𝖻𝖾 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝖾𝗋</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖠𝗇𝗒 𝖵𝖾𝖽𝗂𝗈𝗌 𝖳𝗁𝗎𝗆𝗇𝖺𝗂𝗅𝗌 𝖥𝗋𝗈𝗆 𝖸𝗈𝗎𝗍𝗎𝖻𝖾</b>

<b>Commands and Usage:</b>
» /ytthumb {𝖵𝖾𝖽𝗂𝗈 𝖫𝗂𝗇𝗄}

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/QWiCboxG-Lo</code>
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    ABOOK_TXT = """𝖧𝖾𝗅𝗉 : <b><u>𝖠𝗎𝖽𝗂𝗈 𝖡𝗈𝗈𝗄</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖢𝗈𝗇𝗏𝖾𝗋𝗍 𝖠 𝖯𝖣𝖥 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖠 𝖠𝗎𝖽𝗂𝗈 𝖥𝗂𝗅𝖾 𝚏𝚒𝚕𝚎</b>

<b>Commands and Usage:</b>

• /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝗈𝗋</u></b>

<b>𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝖠 𝖳𝖾𝗑𝗍 𝖳𝗈 𝖠𝗇𝗒 𝖮𝗍𝗁𝖾𝗋 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾𝗌 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍</b>

<b>Commands and Usage:</b>
» /tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

<b>NOTE:</b>
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    RESTRIC_TXT = """𝖧𝖾𝗅𝗉: <b><u>𝖡𝖺𝗇𝗌</u></b>

s𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 𝖻𝖺𝗇𝗇𝖾𝖽; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!

<b>Commands and Usage:</b>
➪ /ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪ /unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪ /tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪ /mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪ /unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪ /tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

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
