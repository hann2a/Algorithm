def location_basic(start_point, arrival_point):
    r1, c1 = start_point
    r2, c2 = arrival_point

    # location_A = ('lu', 'ru',  'ld', 'rd')

    if r2 < r1 and c2 < c1 : # 좌상단
        return 2
    elif r2 < r1 and c2 > c1 : # 우상단
        return 3
    elif r2 > r1 and c2 < c1: # 좌하단
        return 1
    elif r2 > r1 and c2 > c1 : # 우하단
        return 0



import sys
sys.stdin = open('input_1.txt', 'r')

T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip()) # 지도 한 변의 크기
    big_arr = [list(map(int, input().strip().split())) for _ in range(N)]
    # 사과의 위치는 0보다 큰 숫자로 주어진다.

    # 사과 번호별 위치는 미리 할당된 리스트에 차례대로 저장한다.
    # 인덱스 0번은 쓰지 않는다.
    # 이를 고려하여, 크기를 넉넉하게 지정해둔 다음에, 저장
    # 사과는 최대 10개니까, 0 안 쓸거고, 12개로 만든다.
    apple_location_lst = [None] *  12
    apple_location_lst[0] = (0, 0)
    for rdx in range(N):
        for cdx in range(N):
            if big_arr[rdx][cdx] != 0:
                apple_num = big_arr[rdx][cdx]
                apple_location_lst[apple_num] = (rdx,cdx) # 좌표를 튜플로 저장한다.

    # print(apple_location_lst)
    # [(0, 0), (2, 1), (3, 2), (1, 3), None, None, None, None, None, None, None, None]

    '''공통 설정 - 디버깅용'''
    # 화살표 방향
    # arrow = ('right', 'down', 'left' , 'up')

    # 절대적 위치관계
    # location_A = ('ld', 'rd',  'lu', 'ru')


    A = 11 - apple_location_lst.count(None) # 사과 개수
    turn = 0
    now_dir = turn % 4

    for apx in range(A):
        now_dir = turn % 4  # 현재 화살표 방향 갱신
        start_point = apple_location_lst[apx]
        arrival_point = apple_location_lst[apx+1]

        # 절대적 위치관계 확인
        # 함수 활용
        relation_A = location_basic(start_point, arrival_point)

        # 이동축에 대한 위치관계로 변환
        relation_B = (relation_A - now_dir) % 4

        # 상대적 위치관계에 대해, turn 값 확인
        # 딕셔너리 활용
        # 위치관계 : 회전값
        dic = {0 : 1, 1 : 2, 2:3, 3: 3}

        now_turn = dic.get(relation_B)

        # 턴 값에 반영
        turn += now_turn
        # print(f'({start_point})에서 ({arrival_point})로 가야해요. 목적지가 {location_A[relation_A]}에 위치해있는데, 현재 방향이 {arrow[now_dir]}이기 때문에 상대적 위치는 {location_A[relation_B]}입니다. 따라서, 회전은 {now_turn}번 해야해요.'        )


    print(f'#{tc} {turn}')