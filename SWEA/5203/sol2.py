import sys

sys.stdin = open('input.txt', 'r')

def is_triplet(arr):
    for x in arr:
        if x >= 3:
            return True
    return False

def is_run(arr):
    for i in range(8):
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return True
    return False

T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    a_count = [0]*10 # 0 ~ 9까지
    b_count = [0]*10
    winner = 0

    for i, card in enumerate(nums):
        if i % 2 == 0:
            a_count[card] += 1
            if is_triplet(a_count) or is_run(a_count):
                winner = 1
                break
        else:
            b_count[card] += 1
            if is_triplet(b_count) or is_run(b_count):
                winner = 2
                break

    print(f"#{t} {winner}")