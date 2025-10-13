import os, random, requests, sys

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
if not WEBHOOK_URL:
    print("Missing DISCORD_WEBHOOK")
    sys.exit(1)

with open("messages.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f if l.strip()]

message = random.choice(lines)
response = requests.post(WEBHOOK_URL, json={"content": message})
print("Sent:", message, "| Response:", response.status_code)
