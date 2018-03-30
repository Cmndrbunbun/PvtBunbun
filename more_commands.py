import discord, random

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
