import sys

sys.stdin = open('input.txt', 'r')

# 3장이 연속 : triplet
# 3장이 동일한 번호 : run 
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().strip()))

    def triplet(ls): #6개 기준, 숫자 순서대로임을 유의 제일 작은 숫자부터 순서대로 들어옴 
        tri_1 = []
        tri_2 = []
        for s in ls:
            if tri_1 == [] and tri_2 == []:
                tri_1.append(s)
            # 두 번째 
            elif len(tri_1) < 3 and len(tri_1) > 0 and s == tri_1[-1] + 1:
                tri_1.append(s)
            else:
                tri_2.append(s)

        # 3개가 들어왔을 때: 연속된 3개인지 확인
        if len(ls) == 3:
            if (tri_1[0] == tri_1[1] - 1) and (tri_1[1] == tri_1[2] - 1):
                return True
            else:
                return False
            
        # 6개가 들어왔을 때: 두 그룹 모두 triplet이어야 함
        else:
            if (len(tri_1) == 3 and (tri_1[0] == tri_1[1] - 1) and (tri_1[1] == tri_1[2] - 1) and
                len(tri_2) == 3 and (tri_2[0] == tri_2[1] - 1) and (tri_2[1] == tri_2[2] - 1)):
                return True
            else:
                return False
    
    def runny(ls):
        if ls[0] == ls[1] and ls[1] == ls[2]:
            return True 
        else:
            return False 


    # 편의를 위해 정렬 
    numbers.sort() 
    for number in numbers: #123456
        # run 2개인 경우 (+ 6개 다 같을 경우 )
        if (numbers.count(numbers[0]) == 3 and numbers.count(numbers[3]) == 3) or (numbers.count(numbers[0])==6):
            # print('check')
            print(f'#{t} 1')
            break 
        #triplet이 포함된 경우 
        # run + triplet 
        elif runny(numbers[:3]) and triplet(numbers[3:]):
            print(f'#{t} 1')
            break
        elif runny(numbers[3:]) and triplet(numbers[:3]):
            print(f'#{t} 1')
            break
        # triplet + triplet 
        elif triplet(numbers):
            print(f'#{t} 1')
            break
        else:
            print(f'#{t} 0')
            break

# 1번 try : 4번 8번 9번 틀림 
# 123123 (정렬했을 때.... 11 22 33으로 보임) 즉, triplet이 겹치는 숫자를 갖고 있을 때 정렬이 예쁘게 안됨 
# 000000 111111 (숫자가 3 3 이 아니라 6이라 틀림)
# TIL: 반복? 중복도 고려하기 앞으로 
# 드는 생각: 이게맞나? 이렇게 하드코딩하는 게 맞나? 
