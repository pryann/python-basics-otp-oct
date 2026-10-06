# Falsy

print(False == False)  # True
print(False == 0)  # True
print(False == 1)  # False

# # Feladatok

# 1. Írj egy Python programot, amely eltávolítja az összes ismétlődő elemet egy listából és kiírja az eredményt!
values = [1, 2, 3, 4, 5, 2, 3, 6]
unique_values = []

for i in values:
    if i not in unique_values:
        unique_values.append(i)

print(unique_values)
# unique_values = list(set(values))

# 2. Írj egy Python programot, amely kiírja a listában található összes számot, ami 3-mal vagy 4-gyel vagy 5-tel osztható! Használj comrehensiont!
values = [11, 20, 33, 4, 55, 99, 22323, 7]

div = [3, 4, 5]
# filtered_values = [i for i in values for d in div if i % d == 0]
filtered_values = [i for i in values if not i % 3 or not i % 4 or not i % 5]
print(filtered_values)

# 3. Írj egy Python programot, amely egy listából az összes páros és páratlan számot két külön listába szétválasztja! Használj comrehensiont!
# odd = [i for i in values if i % 2 != 0]
odd = [i for i in values if i % 2]
print(odd)
# even = [i for i in values if i % 2 == 0]
even = [i for i in values if not i % 2]
print(even)
