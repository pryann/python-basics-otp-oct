net_prices = [100, 1000, 2000, 5000]
vat_multiplier = 1.27

# gross_prices = []
# for price in net_prices:
#     gross_prices.append(price * vat_multiplier)

gross_prices = [p * vat_multiplier for p in net_prices]

print(gross_prices)

values = [1, 2, 3, 4, 5, 4, 4, 6, 9, 8, 3, 7]
# grades = []

# for i in values:
#     if 0 < i < 6:
#         grades.append(i)

grades = [i for i in values if 0 < i < 6]
print(grades)

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

flatten_matrix = [j for i in matrix for j in i]
print(flatten_matrix)
