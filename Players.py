import json
user_data = {}

def file_user_id(user, uid):
    with open("users_of_quests.json", "w") as f:
        json.dump("User: {}, id: {}\n".format(user, uid), f)