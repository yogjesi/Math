# 2-1 파이썬에서 베이즈 정리 사용하기
# 베이즈 정리 공식 알고 있어야 할 듯
# p_coffee_drinker = 0.65
# p_cancer = 0.005
# p_coffe_drinker_given_cancer = 0.85

# p_cancer_given_coffee_drinker = p_coffe_drinker_given_cancer * p_cancer / p_coffee_drinker

# print(p_cancer_given_coffee_drinker)

# 2-2 사이파이를 사용해 이항 분포 계산하기
# from scipy.stats import binom

# n = 10
# p = 0.9

# # n: 시도 횟수, p: 각 시도의 성공확률, k: 확률을 알고 싶은 성공 횟수

# for k in range(n + 1):
#     probability = binom.pmf(k, n, p)  # pmf = Probability Mass Function(확률 질량 함수)
#     print("{0} - {1}".format(k, probability))

# 0 - 9.999999999999977e-11
# 1 - 8.999999999999976e-09
# 2 - 3.6449999999999933e-07
# 3 - 8.747999999999988e-06
# 4 - 0.00013778099999999974
# 5 - 0.0014880347999999982
# 6 - 0.011160260999999989
# 7 - 0.05739562799999997
# 8 - 0.1937102444999998
# 9 - 0.38742048899999976
# 10 - 0.34867844010000015


# 2-3 사이파이를 사용한 베타 분포
# from scipy.stats import beta

# a = 8
# b = 2

# p = beta.cdf(0.90, a, b)  # cdf = Cumulative Distribution Function (누적 분포 함수)

# print(p)  # 0.7748409780000002

# 2-4 베타 분포에서 오른쪽 면적 구하기
from scipy.stats import beta

a = 8
b = 2

p = 1.0 - beta.cdf(0.90, a, b)

print(p)  # 0.22515902199999982



