user = {
    "name": "John Doe",
    "age": 33,
    "job": "teacher",
}

print(user["name"])
print(user["age"])

user["name"] = "Jane Doe"
print(user)

user["hobbies"] = ["reading", "writing"]
print(user)

user.pop("hobbies")
print(user)

user.update({"id": 1, "job": "developer"})
print(user)

# iterate over the
for i in user:
    print(i)

# for i in user.keys():
#     print(i)

for i in user.values():
    print(i)

print(user.items())
for k, v in user.items():
    print(k, v)
