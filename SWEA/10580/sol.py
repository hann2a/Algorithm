import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    inter = 0

    for first in range(N):
        fs, fe = arr[first]
        for second in range(first+1, N):
            ss, se = arr[second]

            if fs < ss and fe > se:
                inter += 1

            elif fs > ss and fe < se:
                inter += 1

    print(f'#{t} {inter}')