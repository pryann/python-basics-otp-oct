def get_gcd(a, b):
    # if b == 0:
    #     return a
    # else:
    #     print(b, a % b)
    #     return get_gcd(b, a % b)
    return a if b == 0 else get_gcd(b, a % b)


print(get_gcd(100, 12))
