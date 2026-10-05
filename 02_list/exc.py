# 1. Kérj be egy szöveget a felhasználótól, majd írassuk ki az utolsó karakterét!
# feltételezve, hogy nem üres
user_text = input("Adj meg  egy szöveget:")
print(user_text[-1])

print("-----------")

# 2. Írj egy Python programot, amely kiírja egy szöveg minden második karakterét!
text = "lorem ipsum"
for i in range(1, len(text), 2):
    print(text[i])

print("-----------")

# 3. Adott egy `string`, amely szóközöket is tartalmaz. Írj egy programot, amely eltávolítja a szóköz karaktereket a stringből, majd a string karaktereit fordított sorrendben írja ki!
text = "lorem ipsum dolor sit"
without_space = text.replace(" ", "")
for i in range(len(without_space) - 1, -1, -1):
    print(without_space[i])
