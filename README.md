# Ninja Official Txt2Html Bot (Render Web Service)

## Environment variables (Render -> Environment)
- `API_ID`     - from https://my.telegram.org
- `API_HASH`   - from https://my.telegram.org
- `BOT_TOKEN`  - from @BotFather
- `ADMIN_ID`   - your numeric Telegram user ID (bot owner)

## Render setup
1. New -> Web Service -> connect repo (Runtime: **Docker**).
2. Add the 4 environment variables above.
3. Health Check Path: `/health` (optional).
4. Deploy. Use UptimeRobot on the service URL to keep a free instance awake.

## BotFather Commands
```
start - 🚀 Start the bot and check if it is alive
help - 📖 Show the bot guide and all commands
id - 🆔 Get your user, group or channel ID
info - ℹ️ Show your Telegram account information
myplan - 📋 View your premium plan and expiry date
yt2txt - 🎬 Convert a YouTube playlist into a TXT file
cookies - 🍪 Upload YouTube cookies file
rajesh - 📥 Upload a TXT file and download its content
mahar - 📂 Upload a TXT file and download its content
add_channel - ➕ Add a channel or group for bot access
remove_channel - ➖ Remove a channel or group from bot access
stop - 🛑 Stop the current process and restart the bot
logs - 📜 Get the bot log file (Owner only)
adduser - 👤 Add a premium user (Owner only)
removeuser - 🚫 Remove a premium user (Owner only)
users - 👥 List all premium users (Owner only)
allowed_channels - 📋 List all allowed channels and groups (Owner only)
remove_all_channels - 🗑️ Remove all allowed channels and groups (Owner only)
```

Note: premium/channel data is stored in local files, so it resets on redeploy
(Render free disk is ephemeral).
