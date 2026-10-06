# CRUD - Create Read Update Delete

users = [
    {"id": 1, "first_name": "Zared", "last_name": "Pennaman", "email": "zpennaman0@sitemeter.com"},
    {"id": 2, "first_name": "Irving", "last_name": "Pennycock", "email": "ipennycock1@comcast.net"},
    {"id": 3, "first_name": "Garv", "last_name": "Rigge", "email": "grigge2@cloudflare.com"},
    {"id": 4, "first_name": "Dorolice", "last_name": "Brise", "email": "dbrise3@guardian.co.uk"},
    {"id": 5, "first_name": "Tymon", "last_name": "Rookledge", "email": "trookledge4@nih.gov"},
    {"id": 6, "first_name": "Shannah", "last_name": "Eastwell", "email": "seastwell5@typepad.com"},
    {"id": 7, "first_name": "Marjie", "last_name": "Lafee", "email": "mlafee6@eventbrite.com"},
    {"id": 8, "first_name": "Fonzie", "last_name": "Pate", "email": "fpate7@census.gov"},
    {"id": 9, "first_name": "Evvy", "last_name": "Eley", "email": "eeley8@nhs.uk"},
    {"id": 10, "first_name": "Rose", "last_name": "Pittock", "email": "rpittock9@blinklist.com"},
]


def generate_id():
    return max(user["id"] for user in users) + 1


def find_user(user_id):
    for user in users:
        if user_id == user["id"]:
            return user
    # return None


# print(find_user(1))
# print(find_user(11))


def update_user(user_id, payload):
    user = find_user(user_id)
    # if user is not None:
    if user:
        user.update(payload)
        return user


# print(update_user(1, {"first_name": "New  Name"}))


def create_user(payload):
    # user = {"id": max(user["id"] for user in users) + 1}
    # user.update(payload)
    # users.append(user)
    users.append({"id": generate_id(), **payload})
    return users[-1]


print(create_user({"first_name": "John", "last_name": "Doe", "age": 33}))


def remove_user(user_id):
    user = find_user(user_id)
    users.remove(user)
    # return user


remove_user(11)
# print(users)
