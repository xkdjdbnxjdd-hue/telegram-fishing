import sys
import time
import random
from telethon import TelegramClient

# my.telegram.org
api_id = ''
api_hash = ''

async def main():
    h = random.randint(111, 40000)
    async with TelegramClient(f'/sessions/{h}', api_id, api_hash) as client:
        # Вход в акк
        await client.sign_in()
        sys.stdin.readline().strip()
        code = sys.stdin.readline().strip()
        # С кодом я нихуя не придумал, мне лень лол
        if code:
            await client.sign_in(code=code)
        print("[+] FOUND LOGIN!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
