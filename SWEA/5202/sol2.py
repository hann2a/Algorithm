import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    time_table = [tuple(map(int, input().split())) for _ in range(N)]

    end_first = [(end, start) for (start, end) in time_table]
    end_first.sort()

    # print(end_first)

    last_end = 0
    count = 0
    pointer = 0

    while pointer < N:
        end, start = end_first[pointer]

        if start >= last_end:
            count += 1
            last_end = end

        pointer += 1

    print(f'#{t} {count}')