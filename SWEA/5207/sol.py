import sys
sys.stdin = open('input.txt', 'r')

# M개의 정수 중 조건을 만족하는 정수의 개수

def binary_search(target, s, e, prev_dir=0):
    global count, A

    m = (s+e)//2
    if A[m] == target:
        count += 1
        return

    if A[m] < target:
        if prev_dir== 1:
            return
        binary_search(target, m+1, e, 1)

    elif A[m] > target:
        if prev_dir== -1:
            return
        binary_search(target, s, m-1, -1)

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    B = list(map(int, input().split()))

    count = 0

    for num in B:
        binary_search(num, 0, len(A)-1)

    print(f'#{t} {count}')