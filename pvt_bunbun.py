#!/usr/bin/python
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

import discord, re, random
import sys
sys.path.insert(0, '/code_library')
import more_commands, zalgo
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
    print("(" + message.content + ")" + " in channel (" + str(message.channel) + ") on server (" + str(message.server) + ")")

    message_from_user = str(message.content)
    if message.author == client.user:
        return

    if starts_with(message_from_user, author) == False:
        STUFF

    if message_from_user.startswith('!'):
        #Eventually will combine all the "startwith" stuff and move it to another file.
        if message_from_user.startswith('!hello'):
            ret_msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, ret_msg)

        if message_from_user.startswith('!smite'):
            ret_msg = "竜が我が敵を食らう!\nhttps://gph.is/2pMNtmz"
            await client.send_message(message.channel, ret_msg)

        if message_from_user.startswith('!reflect'):
            ret_msg = "竜神の剣をくらえ!\nhttps://gph.is/2J1G8Ze"
            await client.send_message(message.channel, ret_msg)

        if message_from_user.startswith('!pewpew'):
            ret_msg = "https://gph.is/2IZHG62"
            await client.send_message(message.channel, ret_msg)

        if message_from_user.startswith('!roles'):
            ret_msg = ""
            for role in message.author.roles:
                ret_msg = ret_msg + " " + str(role)
            ret_msg = ret_msg.replace("@everyone", "")
            await client.send_message(message.channel, ret_msg)

        if message_from_user.startswith('!clear'):
            auth = more_commands.auth_user(message.author.roles)
            if auth:
                user_msg = message.content.strip("!clear ")
                try:
                    messages_to_delete = int((re.match("(\d+)", user_msg))[1])
                    max_delete = 5
                    if messages_to_delete <= max_delete and messages_to_delete >= 2:
                        mgs = []
                        async for x in client.logs_from(message.channel, limit = messages_to_delete):
                            mgs.append(x)
                        await client.delete_messages(mgs)
                        ret_msg = ""
                    else:
                        ret_msg = "Limit Reached.  Please limit deletion to " + str(max_delete) + " entries."
                except TypeError:
                    ret_msg = "No Number Given. !clear <int>"
            else:
                ret_msg = "Incorrect Role.  Please do not run unauthorized commands."
            if ret_msg is not "":
                await client.send_message(message.channel, ret_msg)


        #Responds to !roll and captures the xdx after to roll a certain amount of dice limited by 20 dice and 100 max limit
        if message_from_user.startswith('!roll'):
            #Remove command string
            user_msg = message.content.strip("!roll ")
            #Format <int>d<int>
            pattern = '(\d+)\s*d\s*(\d+)(\s*[+-]\s*\d+)?'
            try:
                #Pull the amount of dice and then the max roll
                dice_match = re.match(pattern, user_msg)
                times_to_roll = int(dice_match[1])
                die_limit = int(dice_match[2])
                modifier = dice_match[3]
                if modifier is None:
                    modifier = "+0"
                if die_limit <= 100 and times_to_roll <= 20:
                    dice_rolls = []
                    for roll in range(times_to_roll):
                        dice_rolls.append(random.randint(1, die_limit))
                    total_roll = str(eval(str(sum(dice_rolls)) + modifier))
                    modifier = eval(modifier)
                    ret_msg = "Range [" + str(times_to_roll + modifier) + ":" + str(times_to_roll * die_limit + modifier) + "]\nRolls " + str(dice_rolls) + "\nTotal " + total_roll
                    await client.send_message(message.channel, ret_msg)
            except TypeError:
                ret_msg = "Incorrect Format.  !roll <int>d<int> [+ int]"
                await client.send_message(message.channel, ret_msg)

    else:
        ret_msg = search_text(message_from_user)
        await client.send_message(message.channel, ret_msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
