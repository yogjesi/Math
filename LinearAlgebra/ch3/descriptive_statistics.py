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
# sample = [90, 80, 63, 87]
# weights = [1.0, 1.0, 1.0, 2.0]

# weighted_mean = sum(s*w for s, w in zip(sample, weights)) /  sum(weights)

# print(weighted_mean)


# 3-4 파이썬에서 중앙값 계산하기
# sample = [0, 1, 5, 7, 9, 10, 14]

# def median(val):
#     ordered = sorted(val)
#     print(ordered)
#     n = len(ordered)
#     mid = int(n/2) - 1 if n % 2 == 0 else int(n/2)

#     if n% 2 == 0:
#         return (ordered[mid] + ordered[mid+1]) / 2.0
#     else:
#         return ordered[mid]
    
# print(median(sample))


# 3-5 파이썬에서 모드* 계산하기
## *모드? 가장 자주 발생하는 값 집합으로,
## 반복되는 데이터에서 가장 자주 발생하는 값을 찾을 때 유용함
from collections import defaultdict

sample = [1, 3, 2, 5, 7, 0, 2, 3]

def mode(vals):
    counts = defaultdict(lambda: 0)

    for s in vals:
        counts[s] += 1
    
    max_count = max(counts.values())
    modes = [v for v in set(vals) if counts[v] == max_count]
    return modes

print(mode(sample))