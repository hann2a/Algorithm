import sys

sys.stdin = open('input.txt', 'r')

"""
최대 몇 대의 화물차가 이용 가능?
0시부터 24시까지 
"""

T = int(input())

for t in range(1, T+1):
    N = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(N)]

    end_first = [(end, start) for (start, end) in schedule]
    end_first.sort()

    count = 0
    last_end = 0
    pointer = 0
    while pointer < N:
        end, start = end_first[pointer]
        if start >= last_end:
            count += 1
            last_end = end
        pointer += 1

    print(f'#{t} {count}')