import sys

sys.stdin = open('input.txt', 'r')

def merge(left_, right_):
    merged_ = []

    li, ri = 0, 0

    while li < len(left_) and ri < len(right_):

        if left_[li] <= right_[ri]:
            merged_.append(left_[li])
            li += 1
        else:
            merged_.append(right_[ri])
            ri += 1

    merged_.extend(left_[li:])
    merged_.extend(right_[ri:])

    return merged_

def merge_sort(numbers):
    global count

    if len(numbers) <= 1:
        return numbers

    m = len(numbers)//2

    left = numbers[:m]
    right = numbers[m:]

    l_sorted = merge_sort(left)
    r_sorted = merge_sort(right)

    if l_sorted[-1] > r_sorted[-1]:
        count += 1

    return merge(l_sorted, r_sorted)

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input().split()))

    count = 0
    result = merge_sort(numbers)[N//2]

    print(f'#{t} {result} {count}')
