import os

import discord

from commands import help, github

class Client(discord.Client):
  async def on_ready(self):
    print("Ready! Logged-in as {0}".format(self.user))
  async def on_message(self, msg):
    message = str.split(msg.content, " ")
    if message[0] != "xstore":
      return
    selectedMsg = message[1]
    cmds = {
      "help": help.help,
      "github": github.github
    }
    await cmds[selectedMsg](self, msg)

client = Client()
token = os.getenv("TOKEN")
client.run(token)
