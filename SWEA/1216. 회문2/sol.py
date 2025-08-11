import sys

sys.stdin = open("input.txt", "r")

# 가장 긴 회문의 길이를 구하는 문제 
def is_palindrome(s):
        return s == s[::-1]

T = 10

for _ in range(10):
    tc = int(input())
    grid = [input() for _ in range(100)]
    grid_T = list(map(''.join, zip(*grid)))

    # cols = [''.join(arr[r][c] for r in range(100)) for c in range(100)]
    # 회문의 길이 지정 
    for palin_len in range(100, 0, -1):
        is_found = False
        # 회문의 길이가 n 일때 100 x 100의 배열에서 회문 찾기 로직 

        for i in range(100):
            for j in range(100-palin_len+1):
                # s = arr[r][start_c:start_c + palin_len]
                # if s == s[::-1]:
                #     result_palin = palin_len
                #     found = True
                #     break
                if is_palindrome(grid[i][j : j + palin_len]):
                    is_found = True
                    break  

                if is_palindrome(grid_T[i][j : j + palin_len]):
                    is_found = True
                    break 
            if is_found:
                break
        if is_found:
            print(f'#{tc} {palin_len}')
            break