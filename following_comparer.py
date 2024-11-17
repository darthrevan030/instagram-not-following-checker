import json

with open("followers_1.json", "r") as followers_file, open("following.json", "r") as following_file:
    following_data = json.load(following_file)
    followers_data = json.load(followers_file)

def get_usernames_list(json_list):
    usernames = set()
    for user in json_list:
        if 'string_list_data' in user and user['string_list_data']:
            usernames.add(user['string_list_data'][0]['value'].strip().lower())
    return usernames


def get_usernames_dict(json_dict, key):
    usernames = set()
    if key in json_dict:
        for user in json_dict[key]:
            if 'string_list_data' in user and user['string_list_data']:
                usernames.add(user['string_list_data'][0]['value'].strip().lower())
    return usernames

following_usernames = get_usernames_dict(following_data, "relationships_following")
followers_usernames = get_usernames_list(followers_data)

not_following_back = following_usernames - followers_usernames

not_following_back_list = []

for item in not_following_back:
    not_following_back_list.append(item)

with open("not_following_back.txt", "w") as file:
    file.write("Users Not Following Back:\n")
    for user in sorted(not_following_back_list):
        file.write(f"{user}\n")
