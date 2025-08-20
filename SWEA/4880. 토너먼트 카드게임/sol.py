import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input().strip())
    cards = [0] + list(map(int, input().split()))

    # 가위바위보해서 이긴 인덱스를 리턴 
    def srp(i, j):
        a, b = cards[i], cards[j]
        if a == b:
            return i if i< j else j 
        if (a == 1 and b == 3) or (a ==2 and b==1) or (a == 3 and b ==2):
            return i 
        return j 

    # 인덱스가 리턴될 때까지 진행됨 
    # 끝까지 갔을 때 이긴 인덱스를 반환
    def play(l, r):
        if l == r:
            return l
        m = (l + r) //2 
        left = play(l, m)
        right = play(m+1, r)
        return srp(left, right)
    
    winner = play(1, N)
    print(f'#{t} {winner}')