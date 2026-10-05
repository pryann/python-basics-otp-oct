# first_name = "John"
# last_name = "Doe"
# age = 33

first_name, last_name, age = "John", "Doe", 33

print(first_name, last_name, age)


# data swap
a = 10
b = 20

# tmp = a
# a = b
# b = tmp
a, b = b, a

# unpacking strings
abc = "abc"
a, b, c = abc
print(a, b, c)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *_ = numbers
print(first, second)

f, s, *_, l = numbers
print(f, s, l)
