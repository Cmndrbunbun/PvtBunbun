#!/usr/bin/python
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

import discord, re, random, more_commands, zalgo
from discord.ext import commands

#Pull various important data from hidden file.
with open("various_text/private.txt") as f:
    content = f.readlines()

#Pull secret from a hidden txt file.  Not best practice, but better than plain text.
for line in content:
    TOKEN = re.search('Token:(.*)', line).group(1)

#Instantiate the bot and add to client.
client = discord.Client()
bot = commands.Bot(command_prefix='?', description="Discord Bot by CmndrBunbun")

#The "brain" of the bot.  This is always running to hear for commands and key phrases
@client.event
async def on_message(message):
    #Code posted in the CLI for the purpose of logging what is said.  Eventually this will need to output to a logfile.
    print()
    print("(" + message.content + ")" + " in channel (" + str(message.channel) + ") on server (" + str(message.server) + ") by user (" + str(message.author) + ")")

    #Prevent the bot from talking to itself
    message_from_user = str(message.content)
    if message.author == client.user:
        return

    #Bot takes !commands and also listens to all conversations across the server.  This is done with a call to a file filled with the specific
    if message_from_user.startswith('!'):
        await client.send_message(message.channel, more_commands.run_command(message_from_user, message.author))
    else:
        try:
            await client.send_message(message.channel, more_commands.search_text(message_from_user, message.author))
        except Exception as err:
            if '400' in str(err):
                return
            else:
                print("It broke Jim")

#The actual login event for the bot.  This will run on launch of the code to add persistance to the bot.
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
