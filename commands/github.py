import discord

async def github(self, msg):
    embedMsg = discord.Embed(description="Source code available at [GitHub](https://github.com/xstoreapp/discord).", colour=0x000000)
    await msg.channel.send(embed=embedMsg)