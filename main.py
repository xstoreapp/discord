import os

import discord

class Client(discord.Client):
  async def on_ready(self):
    print("Ready! Logged-in as {0}".format(self.user))

client = Client()
token = os.getenv("TOKEN")
client.run(token)
