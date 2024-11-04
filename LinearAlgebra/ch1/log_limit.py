from math import log
from sympy import *

# x = log(8, 2)
# print(x)

# 자연로그가 기본

x = symbols('x')
f = 1/x
result = limit(f, x, oo)
# 심파이에서 무한대 기호는 oo으로 나타냄

print(result)