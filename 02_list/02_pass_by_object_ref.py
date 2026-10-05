a = 33
a_copy = a

#############
# 0x000A 33    <---- a
#              <---- a_copy
############

print(id(a))
print(id(a_copy))

a = 18
print(a, id(a))
print(a_copy, id(a_copy))

#############
# 0x000A 33   <---- a_copy
############
# ax000B       <---- a
############

yearly_salaries = [120_000, 99_000, 67_000, 102_000, 53_000]
yearly_salaries_copy = yearly_salaries
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
#############
# 0x000A [120_000, 99_000, 67_000, 102_000, 53_000]     <---- yearly_salaries
#                                                       <---- yearly_salaries_copy
############

yearly_salaries.append(1_000_000)
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
#############
# 0x000A [120_000, 99_000, 67_000, 102_000, 53_000, 1000000]     <---- yearly_salaries
#                                                                <---- yearly_salaries_copy
############

yearly_salaries_copy.pop()
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
#############
# 0x000A [120_000, 99_000, 67_000, 102_000, 53_000]     <---- yearly_salaries
#                                                       <---- yearly_salaries_copy
############

yearly_salaries = [1, 2, 3]
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
#############
# 0x000A [120_000, 99_000, 67_000, 102_000, 53_000]     <---- yearly_salaries
#                                                       <---- yearly_salaries_copy
############
# 0x00B [1, 2, 3]    <---- yearly_salaries
############
# 0x000A [120_000, 99_000, 67_000, 102_000, 53_000]     <---- yearly_salaries_copy
############
