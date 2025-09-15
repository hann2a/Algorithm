import sys

sys.stdin = open('input.txt', 'r')

def inspection(num):
    string = str(num)
    for i in range(len(str(num))-1):
        if string[i] > string[i+1]:
            return False
    return True 

T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_result = -1 

    for i in range(N):
        for j in range(i+1, N):
            if i < j:
                curr_result = numbers[i] * numbers[j]
                if inspection(curr_result):
                    if max_result < curr_result:
                        max_result = curr_result
        
    print(f'#{t} {max_result}')
