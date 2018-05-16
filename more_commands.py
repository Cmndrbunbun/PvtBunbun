import discord, random, re, zalgo

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
