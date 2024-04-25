from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "7103264571:AAHQABT_b98LJ_tklhwsTLSaPU6OibhTocE")

API_ID = int(os.environ.get("API_ID", "27972068"))

API_HASH = os.environ.get("API_HASH", "6e7e2f5cdddba536b8e603b3155223c1")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
