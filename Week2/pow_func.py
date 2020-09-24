# a ** n
# n = 5
# a_origin = a (create a_origin as a)

# n = n // 2
# if n == 1 or n == 0 -> eliminate
# 5
# 5//2 -> 2
# 2//2 -> 1 eliminate

# with 2:
#     a = a * a = 4
# with 5: (5%2 != 0)
#     a = a * a = 4 * 4 = 16
#     a = a_origin * a = 2 * 16 = 32

def multiply (a, b):
    a = a * b

def power (a, n):
    if (n == 1 or n == 0):
        return
    a_origin = a
    power(a, n // 2)
    multiply(a, a)
    if (n%2 != 0):
        multiply(a, a_origin)

print(pow(2,5))
