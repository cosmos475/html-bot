# Don't Remove Credit Telegram - @Ninja Official
# All secrets come from environment variables (set them in the Render dashboard).
from os import environ


def _required(name):
    value = environ.get(name, "").strip()
    if not value:
        raise SystemExit(
            f"\n[CONFIG ERROR] Environment variable {name} is missing.\n"
            f"Set it in Render -> your service -> Environment, then redeploy.\n"
        )
    return value


API_ID = int(_required("API_ID"))
API_HASH = _required("API_HASH")
BOT_TOKEN = _required("BOT_TOKEN")
ADMIN_ID = int(_required("ADMIN_ID"))  # your numeric Telegram user ID (bot owner)
