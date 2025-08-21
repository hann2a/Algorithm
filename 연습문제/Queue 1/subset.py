from itertools import combinations

arr = list(range(1, 11))
N = len(arr)
target_sum = 10 

valid = []
for k in range(1, N+1):
    for subset in combinations(arr, k):
        if sum(subset) == target_sum:
            valid.append(subset)

valid.sort()

for subset in valid:
    print(*subset)