import discord, random
sys.path.insert(0, '/code_library')
import more_commands, zalgo

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

def search_text(text):
    #Eventually will combine all the "search" stuff and move it to another file.
    if re.search("haha", text, re.IGNORECASE):
        ret_msg = "https://gph.is/2Flp8en"
        await client.send_message(message.channel, ret_msg)

    if re.search("dang", text, re.IGNORECASE):
        if random.randint(1,2) == 1:
            gif = "https://i.imgur.com/BI0qaev.gif"
        else:
            gif = "https://i.imgur.com/Pp4MV32.gif"
        ret_msg = "STOP HERETIC, THIS IS A CHRISTIAN SERVER!\n"+ gif
        await client.send_message(message.channel, ret_msg)

    if re.search("good bot", text, re.IGNORECASE):
        ret_msg = more_commands.good_bot()
        await client.send_message(message.channel, ret_msg)

    if re.search("bad bot", text, re.IGNORECASE):
        message_owner = re.sub("\#\d+", "" , str(message.author))
        bot_message = str(more_commands.good_bot())
        padding_length = int(len(bot_message) / 1.5)
        ret_msg = zalgo.zalgo(1, more_commands.random_string(padding_length) + "\n" + message_owner + " " + bot_message + "\n" + more_commands.random_string(padding_length))
        await client.send_message(message.channel, ret_msg)

    if re.search("zalgo", text, re.IGNORECASE):
        message_from_user = re.sub("zalgo", "", message_from_user, re.IGNORECASE)
        padding_length = int(len(message_from_user) / 1.5)
        if len(message_from_user) > 1:
            ret_msg = zalgo.zalgo(1, more_commands.random_string(padding_length) + "\n" + message_from_user + "\n" + more_commands.random_string(padding_length))
        else:
            ret_msg = zalgo.zalgo(1, more_commands.random_string(padding_length) + "\nTHE ANCIENT ONE STIRS, HE COMES HE COMES\n" + more_commands.random_string(padding_length))
        await client.send_message(message.channel, ret_msg)
