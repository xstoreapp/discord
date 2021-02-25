import os

import discord

import commands

class Client(discord.Client):
  async def on_ready(self):
    print("Ready! Logged-in as {0}".format(self.user))
  async def on_message(self, msg):
    message = str.split(msg.content, " ")
    if message[0] != "xstore":
      return
    selectedMsg = message[1]
    commands[selectedMsg](self, msg)

client = Client()
token = os.getenv("TOKEN")
client.run(token)
