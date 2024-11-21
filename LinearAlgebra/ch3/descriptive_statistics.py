# 3-1
# sample = [1, 3, 2, 5, 7, 0, 2, 3]

# mean = sum(sample) / len(sample)

# print(mean) # 2.875


# 3-2 파이썬에서 가중 평균 계산하기
# sample = [90, 80, 63, 87]
# weights = [0.20, 0.20, 0.20, 0.40]

# weighted_mean = sum(s*w for s, w in zip(sample, weights)) / sum(weights)

# print(weighted_mean) # 81.4


# 3-3 파이썬에서 가중 평균 계산하기
sample = [90, 80, 63, 87]
weights = [1.0, 1.0, 1.0, 2.0]

weighted_mean = sum(s*w for s, w in zip(sample, weights)) /  sum(weights)

print(weighted_mean)


