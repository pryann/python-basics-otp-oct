# # Feladatok

# 1. Írj egy Python függvényt, amely visszaadja az adott stringben található szavak számát!


def word_counter(text: str) -> int:
    return len(text.split())


print(word_counter("lorem ipsum dolor sit amet"))
# 2. Írj egy függvényt, amely egy lista számokat kap bemenetként, majd visszatér egy új listával, amelyben a számok duplűja szerepel.


def doubler(values: list[int | float]) -> list[int | float]:
    return [i * 2 for i in values]


print(doubler([1, 2, 3, 4, 5, 6]))

# 3. Írj egy Python függvényt, amely eldönti, hogy egy adott string palindrom-e vagy sem!
# Használj slicingot!


def is_palindrome(text: str) -> bool:
    lower_case_text = text.lower()
    return lower_case_text == lower_case_text[::-1]


print(is_palindrome("lulul"))
print(is_palindrome("lulu"))


# 4. Készíts egy függvényt, amely paraméterként kap két listát és visszaadja azt a listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek! Comprehensiont használj!
def get_intersection(list_1, list_2):
    return [i for i in list_1 if i in list_2]


list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
print(get_intersection(list_1, list_2))
