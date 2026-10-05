yearly_salaries = [
    120_000,
    99_000,
    67_000,
    102_000,
    53_000,
    44_000,
    119_000,
    88_000,
    204_000,
]

print("to the  2.:", yearly_salaries[:2])
print("from the  2.:", yearly_salaries[2:])
print("from the  2. to the 5.:", yearly_salaries[2:5])
print("from the  1. to the 6., step 2:", yearly_salaries[1:6:2])
print("every second", yearly_salaries[1::2])
print("last element", yearly_salaries[-1])
print("reverse", yearly_salaries[::-1])

# yearly_salaries_copy = yearly_salaries.copy()
yearly_salaries_copy = yearly_salaries[:]
