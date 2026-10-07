#!/bin/sh
# Web server (keeps Render's Web Service port open) + the Telegram bot.
gunicorn app:app --bind 0.0.0.0:${PORT:-10000} --workers 1 --threads 2 --timeout 120 &
exec python3 main.py
