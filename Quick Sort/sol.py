import sys
sys.stdin = open('input.txt', 'r')

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            # 현재 요소를 경계 왼쪽으로 보냄
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i + 1

def quick_sort(arr, start, end):
    if start < end:
        # lomuto partition의 피봇 최종 위치 찾기
        pivot_i = partition(arr, start, end)

        # 정렬하기
        # 피봇을 기준으로 왼쪽 오른쪽을 나눠줌
        quick_sort(arr, start, pivot_i -1)
        quick_sort(arr, pivot_i+1, end)

T = int(input())
for t in range(1, 1+T):
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, len(numbers)-1)
    print(f'#{t}', *numbers)