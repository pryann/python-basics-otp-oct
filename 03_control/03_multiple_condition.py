lang = "Java"

# A   B   A or B
# 0   0     0
# 0   1     1
# 1   0     1
# 1   1     1

# Dont to this
if lang == "Java" or lang == "Python":
    print("Backend")

# better way
backend_languages = ["java", "python"]
if lang.lower().strip() in backend_languages:
    print("Backend")


# A   B   A and B
# 0   0     0
# 0   1     0
# 1   0     0
# 1   1     1

age = 18

if age < 18:
    print("kiskorú")
# elif age >= 18 and age <= 65:
elif 18 <= age <= 65:
    print("felnőtt")
else:
    print("nyugdíjas")


temperature = 50
humidity = 60
rain = True

if temperature > 30 or humidity < 70 and not rain:
    print("Dry")

# not rain            False
# humidity < 70       True
#                     False and True  =  False
# temperature > 30    True
#                     False or True   =   True

if (temperature > 30 or humidity < 70) and not rain:
    print("Dry")
# temperature > 30    True
# humidity < 70       True
#                     True or True     =  True
# not rain            False
#                     True and False   =  False
