import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    count = int(input())
    number = list(map(int, input().split()))

    # 오름차순 정렬 
    def selection_sort(arr):
        for i in range(len(arr)-1): # 마지막은 알아서 정렬되므로 제외 
            min_idx = i

            for j in range(i+1, len(arr)): # 비교할 i 다음의 인자들 
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i] # 더 작은 걸 찾으면 교환 
        return arr
    
    result = selection_sort(number)
    
    print(f"#{test_case}", *result)