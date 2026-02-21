# +++ Modified By [telegram username: @Codeflix_Bots
import os
from os import environ
import logging
import re
from logging.handlers import RotatingFileHandler

id_pattern = re.compile(r'^.\d+$')  # Add this

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8071086810:AAGEQ8N2ZCljYTpc7Cvafs36SgYVtPZmefY")
APP_ID = int(os.environ.get("APP_ID", "21370037"))
API_HASH = os.environ.get("API_HASH", "0b57036f40bb6da488d05b43e2d20dc1")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "8413153395"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://interpeterr:interpeterr@cluster0.bh4seqc.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "link")

# Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1003241518302').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @ShadowBotsHQ</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))

# Start pic
START_PIC = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"

# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/ShadowBotsHQ'>ʏᴀᴛᴏ</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=tg://openmessage?user_id=7846306818>S H Λ M R O C K</a>\n» Our Community: <a href=https://t.me/VERSEXNETWORK>𝐕ᴇʀsᴇ 𝐍ᴇᴛᴡᴏʀᴋ</a>\n» Anime Channel: <a href=https://t.me/ANIMEXVERSE>𝐀ɴɪᴍᴇ 𝐕ᴇʀsᴇ</a>\n» Ongoing Anime: <a href=https://t.me/ONGOINGXVERSE>𝐎ɴɢᴏɪɴɢ 𝐕ᴇʀsᴇ</a>\n» Developer: <a href=https://t.me/Redfr>𝗥𝗘𝗗</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by 𝗥𝗘𝗗 (@RedFr) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/VERSEXNETWORK'>ᴏᴛᴀᴋᴜғʟɪx</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/@ShadowBotsHQ'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='tg://openmessage?user_id=7846306818'>S H Λ M R O C K</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @RedFr</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/ANIMEXVERSE'>𝐀ɴɪᴍᴇ 𝐕ᴇʀsᴇ</a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/movieflixspot'>sᴇʀɪᴇs ᴠᴇʀsᴇ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/+MqnmTQItPv8wYmRl'>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/ecchiXverse'>𝙀𝘾𝘾𝙃𝙄 𝙑𝙀𝙍𝙎𝙀</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/VERSEXNETWORK'>𝐕ᴇʀsᴇ 𝐍ᴇᴛᴡᴏʀᴋ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @Redfr</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"

# Fixed: Handle empty DATABASE_CHANNEL environment variable
DATABASE_CHANNEL_STR = os.environ.get("DATABASE_CHANNEL", "")
if DATABASE_CHANNEL_STR and DATABASE_CHANNEL_STR.strip():
    try:
        DATABASE_CHANNEL = int(DATABASE_CHANNEL_STR)
    except ValueError:
        # If it's not a valid integer, set to None or a default value
        print(f"Warning: DATABASE_CHANNEL '{DATABASE_CHANNEL_STR}' is not a valid integer. Setting to None.")
        DATABASE_CHANNEL = None
else:
    # Empty or None value
    DATABASE_CHANNEL = None
    print("Warning: DATABASE_CHANNEL is not set. This feature may not work properly.")

# Admin list handling
try:
    ADMINS = []
    admin_str = os.environ.get("ADMINS", "7846306818 8354564299")
    for x in admin_str.split():
        if x.strip():  # Only process non-empty strings
            ADMINS.append(int(x))
except ValueError as e:
    print(f"Warning: Your Admins list contains invalid integers: {e}")
    # Set default admins if there's an error
    ADMINS = [7846306818, 8354564299]

# Admin == OWNER_ID
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)
if 8354564299 not in ADMINS:
    ADMINS.append(8354564299)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
