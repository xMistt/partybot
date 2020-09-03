import asyncio
import os
import uvloop

os.system('pip install -U PartyBotPackage')
os.system('clear')

import PartyBotPackage

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = PartyBotPackage.PartyBot(
    device_id=os.getenv('DEVICE_ID'),
    account_id=os.getenv('ACCOUNT_ID'),
    secret=os.getenv('SECRET')
)

try:
    client.run()
except Exception as e:
    print(e)
    print("Failed to login, are you sure you've created a .env file and pasted your device auths? If you're confused, re-watch the tutorial.")
    
