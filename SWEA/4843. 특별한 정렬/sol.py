"""
가장 큰 수, 가장 작은 수, 두 번째 큰 수, 두 번째 작은 수 
10개까지 출력 
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    number = int(input())
    ls = list(map(int, input().split()))
    # 전체 배열을 정리하는 코드 
    def selection_sort(arr):
        for i in range(len(arr)-1):
            # 현재 자리를 최솟값의 위치로 가정 
            min_idx = i 
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j 
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    # 가장 왼쪽 하나, 가장 오른쪽 하나 이런 순서대로 pop해서 result에 넣기 
    pop_ls = selection_sort(ls)
    result_ls = []
    while pop_ls:
        result_ls.append(pop_ls.pop())
        result_ls.append(pop_ls.pop(0))
    # 10보다 길면 자르기 
    if len(result_ls) > 10:
        result_ls = result_ls[:10]
    print(f"#{test_case}", *result_ls)
