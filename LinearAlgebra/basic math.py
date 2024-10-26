# my_value = 2 * (3+2)**2 / 5 - 4
# my_value = 2 * ((3+2)**2 / 5) -4
# print(my_value)

# def f(x):
#     return 2 * x + 1

# x_values = [0, 1, 2, 3]

# for x in x_values:
#     y = f(x)
#     print(y)

from sympy import *
from sympy.plotting import plot3d
# x = symbols('x')
# f = 2*x + 1
# plot(f)

# x = symbols('x')
# f = x**2 + 1
# plot(f)

# x, y = symbols('x y')
# f = 2*x + 2*y
# plot3d(f)

# x = symbols('x')
# expr = x**2 / x**5
# print(expr)

i, n = symbols('i n')

summation = Sum(2*i, (i, 1, n))

up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())