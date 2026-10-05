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
