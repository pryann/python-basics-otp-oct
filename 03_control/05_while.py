# for ciklusváltozó=kezdőérték léptetés:
#   ciklusmag

# ciklusváltozó = kezdőérték
# while feltétel:
#   ciklusmag
#   léptetés

# for i in range(10):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1


while True:
    grade = input("Adj meg egy érdemjegyet (1-5): ")
    if grade.isdigit() and 0 < int(grade) <= 5:
        print("Ez egy érdemjegy")
        break
    print("Próbáld újra Pubi!")
