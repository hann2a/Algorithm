import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    change_stat = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())   # i: 가운데(1-based), j: 양쪽으로 볼 쌍의 개수

        for k in range(1, j+1):            # (i-1-k, i-1+k) 쌍
            left_i  = i - 1 - k
            right_i = i - 1 + k

            # 범위를 벗어나면 더 이상 진행 불가
            if left_i < 0 or right_i >= N:
                break

            # 같은 색이면 둘 다 뒤집기(토글)
            if change_stat[left_i] == change_stat[right_i]:
                change_stat[left_i]  = 1 - change_stat[left_i]
                change_stat[right_i] = 1 - change_stat[right_i]

    print(f'#{t}', *change_stat)



