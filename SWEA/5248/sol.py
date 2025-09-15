import sys
sys.stdin = open('input.txt', 'r')
"""
N은 출석 번호 
M은 신청서 개수 몇 번이 몇 조에 가고 싶은지 
인덱스가 자식 값이 부모 
"""

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    r_x = find_set(x)
    r_y = find_set(y)

    if r_x == r_y:
        return 
    
    if rank[r_x] < rank[r_y]:
        parent[r_x] = r_y

    else:
        parent[r_y] = r_x
        if rank[r_x] == rank[r_y]:
            rank[r_x] += 1

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    submission = list(map(int, input().split()))

    # 최종 부모 노드를 기록할 리스트 
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    
    # 신청서를 읽으면서 parents 업데이트
    for i in range(M):
        p1, p2 = submission[i*2], submission[i*2+1] #  여기 
        # 바로 합 집합으로 만듦
        union(p1, p2)
    print(parent)
    # 조 개수를 세기 위한 로직 
    represent = set()
    for i in range(1, N+1):
        represent.add(find_set(i)) # 여기 
    
    print(f'#{t} {len(represent)}')