# fmt: off
print('banana', type('banana'))
print("banana", type("banana"))

# print('I'am') #Error
print('I\'am')
print("I'am")

#print(""cite"") #Error
print('"cite"')
print("\"cite\"")

# multiline string - pre formatted
print("""first line
         second line""")

print("first line\nsecond line")

print("Gáll " + "Gergely") # concat
print("hello"   * 5) # multiplacation

name  = "John"
age = 33
# My name is John, and I'm 33 years old.
sentence = "My name is " + name + ", and I'm " + str(age) + " years old."
print(sentence)
sentence =  "My name is {}, and I'm {} years old.".format(name, age)
print(sentence)
sentence =  f"My name is {name}, and I'm {age} years old."
print(sentence)

print(name[0])
print(name[3])

# IndexError
# print(name[30])

# TypeError: 'str' object does not support item assignment
# name[0]  = 'j'

print(len(name))

text = "lorem ipsum"
print(f"capitalize: {text.capitalize()}")
print(f"lowercase: {"HELLO".lower()}")
print(f"uppercase: {"hello".upper()}")
print(f"all character all lowercase: {text.islower()}")
print(f"index of 'o': {text.find("o")}")
print(f"count of 'm': {text.count("m")}")
print(f"replace 'o' to 'O': {text.replace("o", "O")}")
print(f"remove whitespace: {'     sdfsf       '.strip()}")


text = text.upper()
print(text)
