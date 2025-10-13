#!/usr/bin/env python3
import os, random, time, requests, sys

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
WEBHOOK_NAME = os.environ.get("WEBHOOK_NAME", "Morton Richard (Webhook Version)")
WEBHOOK_AVATAR = os.environ.get("WEBHOOK_AVATAR", "https://cdn.discordapp.com/attachments/1331452895371202620/1427362318613741638/SPOILER_CD57AD5D-D04B-476A-90E5-1577531C9AF3.jpg?ex=68ee963f&is=68ed44bf&hm=996f57b16bd981bb769598746dfefc0ec5a48675bfb6383803413a86c6b7dc19&")

if not WEBHOOK_URL:
    print("Missing DISCORD_WEBHOOK environment variable.")
    sys.exit(1)

# Load messages
try:
    with open("messages.txt", "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
except FileNotFoundError:
    print("messages.txt not found.")
    sys.exit(2)

# Wait random time (0–1800 seconds = 0–30 min)
delay = random.randint(0, 1800)
print(f"Sleeping {delay//60} minutes {delay%60} seconds before sending...")
# time.sleep(delay)

# Pick random message
message = random.choice(lines)

payload = {
    "content": message,
    "username": WEBHOOK_NAME,
    "avatar_url": WEBHOOK_AVATAR
}

resp = requests.post(WEBHOOK_URL, json=payload)
if resp.status_code in (200, 204):
    print("✅ Sent:", message)
else:
    print("❌ Failed:", resp.status_code, resp.text)
    sys.exit(3)
