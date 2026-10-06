# print, int, type, str, input, range

# print(dir(__builtins__))

# Not defined
# greetings("Johnny")


# def greetings(name):
#     print(f"Hi {name}!")

# greetings("John")
# greetings("Jane")
# greetings("Jack")


def greetings(name):
    return f"Hi {name}!"


print(greetings("Jack"))
result = greetings("Johnny")
print(result)


# default params to the end
def calculate_gross_price(net_price: int, vat_percent: int = 27) -> float:
    return net_price * (1 + vat_percent / 100)


print(calculate_gross_price(1000, 27))
print(calculate_gross_price(10_000, 27))
#  default value ex.
print(calculate_gross_price(5000))
print(calculate_gross_price(1000, 5))
# keyword
print(calculate_gross_price(vat_percent=27, net_price=1000))


# type annotation only doc, not real type checking


def add_value(a: int, b: int) -> int:
    """
    This function sum two integer.

    Args:
        a: The first value.
        b: The second value.

    Returns:
        The sum of values
    """
    print(a + b)


add_value("sdsd", "sfdfdf")


# def calculate_total_price(price: int, vat_percent: int, discount_percent: int) -> float:
#     return price * (1 + vat_percent * 100) * (1 - discount_percent / 100)
