from telethon import TelegramClient

api_id = 'api_id'
api_hash = 'api_hash'
client=TelegramClient('session', api_id, api_hash)
async def main():
    await client.send_message('me', 'Hello,')
    await client.send_file('me', '/home/youssef/Pictures/chess.jpg')


with client:
    client.loop.run_until_complete(main())