a = 10
b = 5

print("a =", a, "\tb =", b)

# a = 1010, b = 0101

# 1010 ^ 0101 (XOR) = 1111 (Decimal 15)
a = a ^ b
print("a ^ b gives", a)

# 1111 ^ 0101 = 1010 (Decimal 10)
b = a ^ b
print("a ^ b gives", b)

# 1111 ^ 1010 = 0101 (Decimal 5)
a = a ^ b
print("a ^ b gives", a)

print("a =", a, "\tb =", b)

