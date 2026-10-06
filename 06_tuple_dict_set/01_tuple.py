# indexed, ordered
# allow duplicated members
# IMMUTABLE

rgb = (255, 255, 0)

print(rgb, type(rgb))
print(rgb[1])

for i in rgb:
    print(i)

# TypeError: 'tuple' object does not support item assignment
# rgb[0] = 0

print(rgb.count(0))
print(rgb.index(0))
print(len(rgb))

# it is not mutation
rgb = (255, 255, 0, 0.5)

# fmt: off
one_element_tuple = (1)
print(type(one_element_tuple))
# fmt: on
one_element_tuple = (1,)
print(type(one_element_tuple))


def stat(values):
    return min(values), max(values), sum(values)


result = stat([1, 2, 3, 4, 5, 6, 7])
print(result, type(result))
