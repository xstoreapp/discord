import discord

async def help(self, msg):
    embedMsg = discord.Embed(title="XStore Help", description="XStore's community first-party bot.", colour=0x000000)
    embedMsg.add_field(name="help", value="This help page")
    embedMsg.add_field(name="github",
        value="This bot is open source. Get the code with this command.")
    embedMsg.set_footer(text="Made by dragonDScript")
    await msg.channel.send(embed=embedMsg)