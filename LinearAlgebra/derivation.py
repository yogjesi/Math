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
# from sympy import *

# x, s = symbols('x s')
# f = x**2

# slope_f = (f.subs(x, x+s)-f) / ((x+s) - x)

# slope_2 = slope_f.subs(x, 2)
# result = limit(slope_2, s, 0)

# print(result)

# 1-23
# from sympy import *
# x, s = symbols('x s')
# f = x**2

# slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)
# result = limit(slope_f, s, 0)

# print(result)

# 1-24
# from sympy import *

# x = symbols('x')
# z = (x**2 + 1)**3 - 2
# dz_dx = diff(z, x)
# print(dz_dx)

# 1-25 연쇄법칙
from sympy import *

x, y = symbols('x y')

# 첫 번째 함수의 도함수
# 충돌을 피하기 위해 _y로 씀
_y = x**2 + 1
dy_dx = diff(_y)

# 두 번재 도함수
z = y**3 - 2
dz_dy = diff(z)

# 연쇄법칙을 사용한 경우와
# 대체 방식을 사용한 경우 도함수 계산
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain= diff(z.subs(y, _y))

# 두 값이 같다는 것을 보임으로써 연쇄 법칙 증명
print(dz_dx_chain)
print(dz_dx_no_chain)