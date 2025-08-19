import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1+T):
    N = int(input())

# 왼쪽으로 랜덤 이동한 방이 어디인지 알려주는 리스트 (순서대로)
p_ls = [0] + list(map(int, input().split()))

# p_ls 사용 계획
# 카운트를 늘려서 몇 번 갔는지 세는 거
room_ls = [0] * (N+1)

# 2부터 N-1까지의 리스트
room_num_ls = []
# print(p_ls)
# 왼쪽 어디로 이동하는지 짝 지어주는 딕셔너리
dict_num = dict()
for i in range(1, N+1):
    dict_num[i] = p_ls[i]

for i in range(2, N):
    room_num_ls.append(i)

# moving : 지금 방 어디에 가고 있는지 조준하는 포인터
moving = 1
while moving != N:
    # 1번방에 들어갔을 때
    # 카운트를 세고
    # 바로 2번방으로 이동한다
    if moving == 1:
        room_ls[1] += 1
        moving += 1
    # 만약 2부터 n-1번방까지 중 하나라면
    # 카운트를 늘리고
    # 만약 카운트 늘렸을 때 1이면 왼쪽으로 가는 포탈 중 하나를 이용
    # 1이 아니라면 바로 오른쪽으로 간다
    elif moving in room_num_ls:
        room_ls[moving] += 1
        if room_ls[moving] == 1:
            moving = dict_num[moving]
        else:
            moving += 1
    elif moving == 0:
        moving = 1

# moving이 N을 가리켜서 빠져나왔다면
portal_result = sum(room_ls)
print(f'#{t} {portal_result}')