# unindexed, unordered
# contains unique values


my_set = {1, 2, 3}
print(my_set, type(my_set))

# TypeError: 'set' object is not subscriptable
# print(my_set[1])

my_set.add(4)
print(my_set)

my_set.update([5, 6, 7])
print(my_set)

# KeyError if not exists
my_set.remove(1)
print(my_set)

# not raise error if not exists
my_set.discard(2)
print(my_set)

# remove a random element
my_set.pop()
print(my_set)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))  # |
print(x1.intersection(x2))  # &
print(x1.difference(x2))  # -
print(x1.symmetric_difference(x2))  # ^
print({"s"}.isdisjoint(x2))  #
print(x1.issubset({"a", "b", "c", "d"}))  # <=
print({"a", "b", "c", "d"}.issuperset(x1))  # >

for i in x1:
    print(i)
