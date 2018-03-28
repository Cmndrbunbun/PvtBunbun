#!/usr/bin/python
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

import discord, re, random
from discord.ext import commands

with open("private.txt") as f:
    content = f.readlines()

for line in content:
    TOKEN = re.search('Token:(.*)', line).group(1)

client = discord.Client()
bot = commands.Bot(command_prefix='?', description="Test Bot by CmndrBunbun")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        ret_msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, ret_msg)

    if message.content.startswith('!smite'):
        ret_msg = "竜が我が敵を食らう!\nhttps://gph.is/2pMNtmz"
        await client.send_message(message.channel, ret_msg)

    if message.content.startswith('!reflect'):
        ret_msg = "竜神の剣をくらえ!\nhttps://gph.is/2J1G8Ze"
        await client.send_message(message.channel, ret_msg)

    if message.content.startswith('!pewpew'):
        ret_msg = "https://gph.is/2IZHG62"
        await client.send_message(message.channel, ret_msg)

    #Responds to !roll and captures the xdx after to roll a certain amount of dice limited by 20 dice and 100 max limit
    if message.content.startswith('!roll'):
        #Remove command string
        user_msg = message.content.strip("!roll ")
        #Format <int>d<int>
        pattern = '(\d+)\s*d\s*(\d+)\s*\+?\s*(\d*)'
        try:
            #Pull the amount of dice and then the max roll
            dice_match = re.match(pattern, user_msg)
            times_to_roll = int(dice_match.group(1))
            die_limit = int(dice_match.group(2))
            if dice_match.group(3):
                modifier = int(dice_match.group(3))
            else:
                modifier = None
            if die_limit <= 100 and times_to_roll <= 20:
                dice_rolls = []
                for roll in range(times_to_roll):
                    if modifier is not None:
                        dice_rolls.append(random.randint(1, die_limit) + modifier)
                    else:
                        dice_rolls.append(random.randint(1, die_limit))
                clean_roll = ""
                for roll in dice_rolls:
                    clean_roll = clean_roll + " " + str(roll)
                if modifier:
                    clean_roll = clean_roll + " (" + str(modifier) + ")"

                await client.send_message(message.channel, clean_roll)
        except:
            ret_msg = "Incorrect Format.  !roll <int>d<int>"
            await client.send_message(message.channel, ret_msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
