# def count_by(x, n):
#     ans = []
#     for num in range(x, x*n + 1, x):
#         ans.append(num)
#     print(ans)

# count_by(1, 10)
# count_by(2, 5)

# ========================================

# using a loop to add up a numbers of a list
# ans = 0
# list = [1, 3, 5, 6, 2]

# for number in list:
#   ans += number

# print(ans)

# ========================================

# calcular el volumen de cilindro

# import math

# def cilindroVolumen (r, h):
#   return r * r * math.pi * h

# print(cilindroVolumen(2, 4))


# cilindroVolumen = lambda r, h: r * r * math.pi * h
# print(cilindroVolumen(2, 4))

# ========================================


# -----map-----
numeros = (1, 2, 3, 4, 5)

def cubico(number):
    return number**3

result = map(cubico, numeros)
print(list(result))

# resultLambda = map(lambda cubico, numeros: )

# -----filter-----
numeros = [1, 2, 3, 4, 5]
result = filter(lambda x: x > 5, numeros)

# -----reduce-----
from functools import reduce

numeros = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numeros)
print(result)

