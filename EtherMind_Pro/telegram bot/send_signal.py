# Phase 1: Telegram Signal Sender
# File: send_signal.py

import telepot

BOT_TOKEN = '8073503678:AAFpPYsRLugPVFTBq7h7QOJNfUql_yCqy5g'
CHAT_ID = '7480633262'

message = """📢 বাইনারি ট্রেডিং সিগন্যাল:
USD/JPY
📈 CALL (Buy)
🕐 15 Minute"""

bot = telepot.Bot(BOT_TOKEN)
bot.sendMessage(CHAT_ID, message)
print("✅ Signal পাঠানো হয়েছে Telegram-এ!")
