## 1.11 적분

# 1-26 파이썬으로 적분 근사
# def approximate_integral(a, b, n, f):
#     delta_x = (b - a) / n
#     total_sum = 0

#     for i in range(1, n + 1):
#         midpoint = 0.5 * (2 * a + delta_x * (2*i-1))
#         total_sum += f(midpoint)

#     return total_sum * delta_x

# def my_function(x):
#     return x**2 + 1

# area = approximate_integral(a=0, b=1, n=5, f=my_function)

# print(area)

# # 1-27
# area = approximate_integral(a=0, b=1, n=1000, f=my_function)

# print (area)

# # 1-28
# area = approximate_integral(a=0, b=1, n=1_000_000, f=my_function)

# print(area)

# 1-29 심파이로  적분 수행
# from sympy import *

# x = symbols('x')

# f = x**2 + 1

# area = integrate(f, (x, 0, 1))

# print(area)

# 1-30 극한을 사용해 적분 계산
from sympy import *

# 선언부
x, i, n = symbols('x i n')

f = x**2 + 1
lower, upper = 0, 1

# 상자의 너비와 i 위치에 있는 직사각형의 높이 계산
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# n개의 직사각형을 순환하면서 면적을 더함
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# 직사각형의 개수 n을 무한대로 늘려 면적 계산
area = limit(n_rectangles, n, oo)

print(area)