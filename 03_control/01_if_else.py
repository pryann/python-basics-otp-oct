print(type(False))
print(type(True))

yearly_salary_in_usd = 10_000
high_salary_threshold = 100_000

# HA feltétel  Igaz:
#   csináld ezt

#  ==, !=, >, <, >=, <=, is, in, is not, not in
if yearly_salary_in_usd > high_salary_threshold:
    print("High salary")
else:
    print("Low  salary")


grade = input("Adj meg egy érdemjegyet (1-5):  ")
if grade == "1":
    print("Elégtelen")
elif grade == "2":
    print("Elégséges")
elif grade == "3":
    print("Közepes")
elif grade == "4":
    print("Jó")
elif grade == "5":
    print("Jeles")
else:
    print("Ez nem érdemjegy")
