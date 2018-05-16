#!/usr/bin/python
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

import discord, re, random, more_commands, zalgo
from discord.ext import commands

with open("various_text/private.txt") as f:
    content = f.readlines()

for line in content:
    TOKEN = re.search('Token:(.*)', line).group(1)

client = discord.Client()
bot = commands.Bot(command_prefix='?', description="Discord Bot by CmndrBunbun")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    print()
    print("(" + message.content + ")" + " in channel (" + str(message.channel) + ") on server (" + str(message.server) + ") by user (" + str(message.author) + ")")

    message_from_user = str(message.content)
    if message.author == client.user:
        return

    if message_from_user.startswith('!'):
        ret_msg = more_commands.run_command(message_from_user, message.author)
        await client.send_message(message.channel, ret_msg)
    else:
        try:
            ret_msg = more_commands.search_text(message_from_user, message.author)
            await client.send_message(message.channel, ret_msg)
        except Exception as err:
            if '400' in str(err):
                return
            else:
                print("It broke Jim")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
