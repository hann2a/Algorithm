import sys, itertools 

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for_one = int(N/2) 
    ingredient = list(range(N))

    # a, b : 재료 모음 
    a = []
    b = []
    for i in itertools.combinations(ingredient, for_one):
        a.append(i) # 튜플 묶음으로 .. 

    for mini_a in a:
        b.append(tuple(sorted(set(ingredient) - set(mini_a))))

    
    # 최소 
    min_diff = float('inf')

    # 그 개수만큼 시너지가 생김 
    for i in range(len(a)//2): # 각 조합 리스트의 첫 번째 합부터 구함 
        synergy_a = 0
        synergy_b = 0

        a_com = a[i] # (8, 9, 10, 11, 12, 13, 14, 15)
        for first, second in itertools.permutations(a[i], 2):  # (8, 9)
            synergy_a += arr[first][second]

        b_com = b[i] # (0, 1, 2, 3, 4, 5, 6, 7)
        for f, s in itertools.permutations(b[i], 2):
            synergy_b += arr[f][s]

        if abs(synergy_a - synergy_b) < min_diff:
            min_diff = abs(synergy_a - synergy_b)
    
    print(f'#{t} {min_diff}')
        

