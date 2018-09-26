import discord, re, random, zalgo
from riotwatcher import RiotWatcher

def good_bot():
    responses = []
    #All responses are pulled from Friendly Bot on Reddit.  See reddit.com/user/friendly-bot for the source
    with open ('various_text/good_bot_responses.txt', encoding="UTF-8") as f:
        responses = f.readlines()
    responses = [li.strip() for li in responses]

    index = random.randint(1, len(responses) - 1)
    return responses[index]

def auth_user(user_roles_to_auth):
    auth = False
    for role in user_roles_to_auth:
        if role.name == "Admin":
            auth = True
    return auth

def random_string(length):
    string_of_chars = ""
    for character in range(length):
        string_of_chars = string_of_chars + " " + (str(chr(random.randint(32, 126))))
    return string_of_chars

def search_text(text, author):
    #Eventually will combine all the "search" stuff and move it to another file.
    if re.search("haha", text, re.IGNORECASE):
        return "https://gph.is/2Flp8en"
    elif re.search("dang", text, re.IGNORECASE):
        if random.randint(1,2) == 1:
            gif = "https://i.imgur.com/BI0qaev.gif"
        else:
            gif = "https://i.imgur.com/Pp4MV32.gif"
        return "STOP HERETIC, THIS IS A CHRISTIAN SERVER!\n" + gif
    elif re.search("good bot", text, re.IGNORECASE):
        return good_bot()
    elif re.search("bad bot", text, re.IGNORECASE):
        message_owner = re.sub("\#\d+", "" , str(author))
        bot_message = str(good_bot())
        padding_length = int(len(bot_message) / 1.5)
        return zalgo.zalgo(1, random_string(padding_length) + "\n" + message_owner + " " + bot_message + "\n" + random_string(padding_length))
    elif re.search("zalgo", text, re.IGNORECASE):
        message_from_user = re.sub("zalgo", "", text, re.IGNORECASE)
        padding_length = int(len(message_from_user) / 1.5)
        if len(message_from_user) > 1:
            return zalgo.zalgo(1, random_string(padding_length) + "\n" + message_from_user + "\n" + random_string(padding_length))
        else:
            return zalgo.zalgo(1, random_string(padding_length) + "\nTHE ANCIENT ONE STIRS, HE COMES HE COMES\n" + random_string(padding_length))

def run_command(text, author):
    #Eventually will combine all the "startwith" stuff and move it to another file.
    if text.startswith('!hello'):
        return 'Hello {0.author.mention}'.format(text)
    elif text.startswith('!smite'):
        return "竜が我が敵を食らう!\nhttps://gph.is/2pMNtmz"
    elif text.startswith('!reflect'):
        return "竜神の剣をくらえ!\nhttps://gph.is/2J1G8Ze"
    elif text.startswith('!pewpew'):
        return "https://gph.is/2IZHG62"
    elif text.startswith('!roles'):
        ret_msg = ""
        for role in author.roles:
            ret_msg = ret_msg + " " + str(role)
        ret_msg = ret_msg.replace("@everyone", "")
        return ret_msg
    #Responds to !roll and captures the xdx after to roll a certain amount of dice limited by 20 dice and 100 max limit
    elif text.startswith('!roll'):
        #Remove command string
        user_msg = text.strip("!roll ")
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
                if times_to_roll == 1:
                    return "Range [" + str(times_to_roll + modifier) + ":" + str(times_to_roll * die_limit + modifier) + "]\nRoll " + str(dice_rolls)
                else:
                    return "Range [" + str(times_to_roll + modifier) + ":" + str(times_to_roll * die_limit + modifier) + "]\nRolls " + str(dice_rolls) + "\nTotal " + total_roll
        except TypeError:
            if user_msg == "":
                return "Range [1:20]\nRoll " + str(random.randint(1, 20))
            return "Incorrect Format.  !roll <int>d<int> [+ int]"
    elif text.startswith('!riot'):
        #Input = !riot SUMMONER_NAME REGION
        with open("various_text/riot.txt") as f:
            content = f.readlines()
        #Pull secret from a hidden txt file.  Not best practice, but better than plain text.
        for line in content:
            KEY = re.search('Riot:(.*)', line).group(1)
        watcher = RiotWatcher(KEY)
        region = 'na1'
        user_msg = text.strip("!riot ")
        summoner = watcher.summoner.by_name(region, user_msg)
        ranked_stats = watcher.league.positions_by_summoner(region, summoner['id'])
        return str(summoner) + "\n\n" + str(ranked_stats)
    else:
        return "No correct command was given"
