yearly_salaries = [
    120_000,
    99_000,
    67_000,
    102_000,
    53_000,
]
high_salary_threshold = 100_000
sum_low_salaries = 0
sum_high_salaries = 0

for salary in yearly_salaries:
    if salary < high_salary_threshold:
        sum_low_salaries += salary
    else:
        sum_high_salaries += salary

print(sum_low_salaries)
print(sum_high_salaries)
