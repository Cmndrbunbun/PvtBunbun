import discord, random

def good_bot():
    responses = []
    #All responses are pulled from Friendly Bot on Reddit.  See reddit.com/user/friendly-bot for the source
    with open ('good_bot_responses.txt', encoding="UTF-8") as f:
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
