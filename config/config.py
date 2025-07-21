import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23470912"))
API_HASH = getenv("API_HASH", "33ac02b7891c5396e6b305802d56cf4f")
BOT_TOKEN = getenv("BOT_TOKEN", "8025984970:AAE48m0S5uGdxsN0Z6VxJyZSvRt9_YzJcQM")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002894584465"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Expert Music")

OWNER_ID = list(map(int, getenv("OWNER_ID", "7800338935").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "Music")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamYukki/YukkiMusicBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)
SUPPORT_GROUP = getenv("SUPPORT_GROUP", None)

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", None)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

SET_CMDS = getenv("SET_CMDS", "False").lower() == "true"

STRING1 = getenv("STRING_SESSION1", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []

START_IMG_URL = getenv("START_IMG_URL", None)
PING_IMG_URL = getenv("PING_IMG_URL", "assets/Ping.jpeg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "assets/Playlist.jpeg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "assets/Global.jpeg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "assets/Stats.jpeg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "assets/Audio.jpeg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "assets/Video.jpeg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "assets/Stream.jpeg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "assets/Soundcloud.jpeg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "assets/Youtube.jpeg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "assets/SpotifyArtist.jpeg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "assets/SpotifyAlbum.jpeg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "assets/SpotifyPlaylist.jpeg")


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))


def validate_url(name, url):
    if url and not re.match(r"^(http|https)://", url):
        print(f"[ERROR] - Your {name} is invalid. It must start with https://")
        sys.exit()


validate_url("SUPPORT_CHANNEL", SUPPORT_CHANNEL)
validate_url("SUPPORT_GROUP", SUPPORT_GROUP)
validate_url("UPSTREAM_REPO", UPSTREAM_REPO)
validate_url("GITHUB_REPO", GITHUB_REPO)

if PING_IMG_URL != "assets/Ping.jpeg":
    validate_url("PING_IMG_URL", PING_IMG_URL)

if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
    validate_url("PLAYLIST_IMG_URL", PLAYLIST_IMG_URL)

if GLOBAL_IMG_URL != "assets/Global.jpeg":
    validate_url("GLOBAL_IMG_URL", GLOBAL_IMG_URL)

if STATS_IMG_URL != "assets/Stats.jpeg":
    validate_url("STATS_IMG_URL", STATS_IMG_URL)

if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
    validate_url("TELEGRAM_AUDIO_URL", TELEGRAM_AUDIO_URL)

if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
    validate_url("TELEGRAM_VIDEO_URL", TELEGRAM_VIDEO_URL)

if STREAM_IMG_URL != "assets/Stream.jpeg":
    validate_url("STREAM_IMG_URL", STREAM_IMG_URL)

if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
    validate_url("SOUNCLOUD_IMG_URL", SOUNCLOUD_IMG_URL)

if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
    validate_url("YOUTUBE_IMG_URL", YOUTUBE_IMG_URL)

if not MUSIC_BOT_NAME.isascii():
    print("[ERROR] - MUSIC_BOT_NAME contains special characters. Please use only standard characters.")
    sys.exit()
