import sys
from itertools import combinations
sys.stdin = open('input.txt')
"""
선반의 높이 B (1~점원들 키의 합) 
점원의 수 N (1~20)
"""

T = int(input())

for t in range(1, 1+T):
    N, B = map(int, input().split())
    heights = list(map(int,input().split()))

    lowest = float('inf')
    best = False

    for i in range(1, N+1):
        for subset in combinations(heights, i):
            check_sum = sum(subset)
            if check_sum >= B and check_sum < lowest:
                lowest = check_sum

                if check_sum == B:
                    lowest = check_sum
                    best = True
                    break
        if best:
            break

    print(f'#{t} {lowest - B}')
