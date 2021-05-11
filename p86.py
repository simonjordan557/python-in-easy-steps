import math, random

print('Rounded Down 9.5:', math.floor(9.5))
print('Rounded Up 9.5:', math.ceil(9.5))

num = 4
print(num, 'Squared:', math.pow(num, 2))
print(num, 'Square Root:', math.sqrt(num))

ran = random.random()
print('Single Random Number:', ran)

nums = random.sample(range(1, 50), 6)
nums.sort()

print('Your Lucky Lotto Numbers Are:', nums)
