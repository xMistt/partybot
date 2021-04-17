import asyncio
import os
import sys

env_vars = {}
if os.path.isfile('.auth'):
    with open('.auth') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.replace("\"", "")
else:
  print("You're missing the \".auth\" file, if you have a \".env\" file rename it to \".auth\".")
  sys.exit()

os.system('pip install certifi')
os.system('pip install -U PartyBotPackage')
os.system('clear')

import uvloop
import PartyBotPackage

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = PartyBotPackage.PartyBot(
    device_id=env_vars['DEVICE_ID'],
    account_id=env_vars['ACCOUNT_ID'],
    secret=env_vars['SECRET']
)

try:
    client.run()
except Exception as e:
    print(e)
    print("Failed to login, your device auths are probably invalid, please "
          "try again and make new ones.\nIf you're confused, re-watch the "
          "tutorial.")
    print(env_vars)
