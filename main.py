import asyncio
import os
import uvloop

os.system('pip install -U PartyBotPackage==0.1.9')
os.system('clear')

import PartyBotPackage

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = PartyBotPackage.PartyBot(
    device_id=os.getenv('DEVICE_ID'),
    account_id=os.getenv('ACCOUNT_ID'),
    secret=os.getenv('SECRET')
)

client.run()
