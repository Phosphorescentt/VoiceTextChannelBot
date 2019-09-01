import sqlite3

import discord
from discord.ext import commands

from SECRETS import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.commands = {"create_channel": self.create_channel}

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        message.content = message.content.lower()

        if message.content.startswith(">>>"):
            guild = message.guild
            command_raw = message.content.replace(">>>", "")
            command = command_raw.split()
    
            try:
                execute = self.commands[command[0]]
                await execute(guild, command)
            except KeyError as e:
                print(e)

    async def create_channel(self, guild, command):
        await guild.create_text_channel(name=command[1])
        await guild.create_voice_channel(name=command[1])


client = MyClient()
client.run(token)
