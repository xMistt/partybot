import asyncio
import PartyBotPackage

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = PartyBotPackage.PartyBot(
    device_id="",
    account_id="",
    secret=""
)

client.run()
