import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

"""
N: 화덕에서 구울 수 있는 피자 개수 
M: 주어진 피자의 개수 
"""
for t in range(1, T+1):
    N, M = map(int, input().split())
    pizza_cheeze = list(map(int, input().split()))
    
    # 인덱스를 위해 0:0을 추가해놓는다 
    pizza_num = {0:0}
    # 번호와 치즈 양이 매칭된 딕트를 만들어보자 
    # 1번부터 시작함 
    for i in range(M):
        for cheeze in pizza_cheeze:
            pizza_num[i+1] = pizza_cheeze[i]

    
    # 화덕이 다 찰 때까지 피자를 처음으로 채움 
    count = 0 
    oven = []
    left = []
    for i in range(1, M+1): # 총 피자 개수만큼 1부터 돈다
        if count < N:
            oven.append([i, pizza_num[i]])
            count += 1
        else:
            left.append([i, pizza_num[i]])
    
    # print(f'피자 치즈 리스트에 {pizza_num}가 들어있습니다')
    # print(f'오븐에 {oven} 가 들어있습니다!')
    # print(f'남은 피자리스트는 {left} 다음과 같습니다')


    # pointer가 0인 곳에서 피자 확인 
    pointer = 0
    # 끝나는 조건: 만약 오븐에 리스트의 1번 인덱스 값이 0이 아닌 값이 하나 남았을 때 종료 
    # 이걸 어떻게 확인함..?
    # 못 확인해서 그냥 오븐에 0 같은 거 추가 안하고 없애 버리고 오븐에 피자 하나 남았을 때 기준으로 함 
    while len(oven) > 1:
        # 포인터가 0부터 가리키기 시작 
        oven[pointer][1] //= 2 
        # 만약 가리킨 피자의 치즈가 0이 아니라면 2로 나눈 몫 
        if oven[pointer][1] == 0:
            if left:
                oven[pointer] = left.pop(0)
            else:
                del oven[pointer]
                if pointer >= len(oven):
                    pointer = 0
        else: 
            pointer = (pointer +1) % len(oven)

    print(f'#{t} {oven[0][0]}')