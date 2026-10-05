# ordered
# indexed
# mutable
# allow duplicated members

# test = [
#     "hello",
#     12,
#     12.12,
#     True,
#     [1, 2, 3],
#     "",
# ]

yearly_salaries = [
    120_000,
    99_000,
    67_000,
    102_000,
    53_000,
]

print(type(yearly_salaries), yearly_salaries)
print(yearly_salaries[0])
print(yearly_salaries[3])
print(len(yearly_salaries))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

yearly_salaries[0] = 0
print(yearly_salaries)

# elem hozzáfűzése a végéhez
yearly_salaries.append(200_000)
print(yearly_salaries)

# elemek hozzáfűzése
yearly_salaries.extend([10_000, 20_000])
print(yearly_salaries)

# hozzáadás adott pozícióba
yearly_salaries.insert(1, 1111)
print(yearly_salaries)

# adott érték eltávolítása
yearly_salaries.remove(1111)
print(yearly_salaries)

# index alapú törlés
del yearly_salaries[0]
print(yearly_salaries)

# remove element by index, default -1, the last element
yearly_salaries.pop(2)
print(yearly_salaries)

# számosság
yearly_salaries.append(10_000)
yearly_salaries.append(10_000)
print(yearly_salaries)
print(f"count of '10_000:  {yearly_salaries.count(10_000)}")

yearly_salaries.sort(reverse=True)
print(yearly_salaries)

yearly_salaries.reverse()
print(yearly_salaries)

text = "My name is John Doe."
words = text.split()
print(words)

concated = " ".join(words)
print(concated)
