import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    length = int(input())
    seq = input().strip()

    max_count = 0 
    count = 0
    for num in seq:
        if num  == '1':
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0 
    max_count = max(max_count, count)
    print(f'#{t} {max_count}')