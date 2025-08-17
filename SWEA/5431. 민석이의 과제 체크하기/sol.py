import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    submitted = list(map(int, input().split()))

    # 과제를 제출하지 않은 사람의 번호 오름차순으로 출력 
    final_ls = []
    for person in range(1, N+1):
        if person in submitted:
            pass
        else:
            final_ls.append(person)
    
    final_ls.sort()

    print(f'#{t}', *final_ls)