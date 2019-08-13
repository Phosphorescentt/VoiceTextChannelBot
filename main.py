import sqlite3

import discord
from discord.ext import commands

from SECRETS import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith(">>>"):
            message.content = message.content.replace(">>>", "")
            guild = message.guild
            await guild.create_text_channel(name=message.content)
            await guild.create_voice_channel(name=message.content)


client = MyClient()
client.run(token)
