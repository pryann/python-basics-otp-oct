from tkinter.messagebox import RETRY


def get_minimum(values: list[int]) -> int:
    if not values:
        raise ValueError("The list is empty")

    min_value = values[0]
    for value in values[1:]:
        if value < min_value:
            min_value = value
    return min_value


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_minimum(values))
# print(get_minimum([]))
print(min(values))


def get_maximum(values):
    if not values:
        raise ValueError("The list is empty")

    max_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
    return max_value


print(get_maximum(values))
print(max(values))


def summa(values):
    sum_values = 0
    for value in values:
        sum_values += value
    return sum_values


print(summa(values))
print(sum(values))


def average(values):
    summa(values) / len(values)


def count_values(values, search):
    counter = 0
    for value in values:
        if value == search:
            counter += 1
    return counter


print(count_values(values, 1))
print(values.count(1))


def get_index(values, search):
    for i, v in enumerate(values):
        if v == search:
            return i


print(get_index(values, 1))
print(values.index(1))


def is_contains(values, search):
    for value in values:
        if value == search:
            return True
    return False


print(is_contains(values, 1))
print(is_contains(values, 10))

print(1 in values)
print(10 in values)
