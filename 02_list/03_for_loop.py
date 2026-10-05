for i in range(10):
    print(i)

for i in range(10, 20):
    print(i)

for i in range(10, 20, 2):
    print(i)


for i in range(10, 0, -1):
    print(i)

net_prices = [100, 1000, 2000, 5000]
gross_prices = []
tax_multiplier = 1.27

# ha az összes  elem kell
for price in net_prices:
    gross_prices.append(price * tax_multiplier)

print(gross_prices)

# ha nem kell mind
for i in range(0, len(net_prices), 2):
    print(net_prices[i])

# index és value
for i, v in enumerate(net_prices):
    print(f"index: {i},  value: {v}")
