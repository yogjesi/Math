# 미분 계산하기
# def derivative_x(f, x, step_size):
#     m = (f(x + step_size) - f(x)) / ((x + step_size) -x)
#     return m

# def my_function(x):
#     return x**2

# slope_at_2 = derivative_x(my_function, 2, 0.00001)

# print(slope_at_2)

# 1-18
# from sympy import *

# x = symbols('x')
# f = x**2
# dx_f = diff(f)  ## 여기서 도함수 계산
# print(dx_f)


# 1-19
# def f(x):
#     return x**2

# def dx_f(x):
#     return 2*x

# slope_at_2 = dx_f(2.0)

# print(slope_at_2)

# 1-20
# print(dx_f.subs(x, 2)) # 1-18 코드 살려서

# 1-21
# from sympy import *
# from sympy.plotting import plot3d

# x, y = symbols('x y')
# f = 2*x**3 + 3*y**3

# dx_f = diff(f, x) # 식 f를 x에 대해 미분
# dy_f = diff(f, y) # 식 f를 y에 대해 미분

# # 아래에서 편도함수 두 개 나오고 그래프 하나 그려주고.
# print(dx_f)
# print(dy_f)

# plot3d(f)

# 1-22
from sympy import *

x, s = symbols('x s')
f = x**2

slope_f = (f.subs(x, x+s)-f) / ((x+s) - x)

slope_2 = slope_f.subs(x, 2)
result = limit(slope_2, s, 0)

print(result)