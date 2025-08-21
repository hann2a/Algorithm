from itertools import combinations

# 원본 배열 
arr = list(range(1, 11))
N = len(arr)
target_sum = 10 

# 조건에 맞는 모든 부분집합을 찾아 리스트에 저장 
valid = []
for k in range(1, N+1):
    # arr에서 k개의 원소로 만들 수 있는 모든 조합 생성 
    # combination(iterable, r) 
    # iterable 객체에서 r개를 뽑는 조합을 구할 수 있다 
    # generator 형식으로 반환, list 자료형으로 변환하여 사용 
    # 순서대로 
    for subset in combinations(arr, k):
        # 해당 조합의 합이 10이면
        if sum(subset) == target_sum:
            # 바로 출력하지 않고, 결과 리스트에 추가 
            valid.append(subset)

# 찾은 부분집합들을 python의 기본 정렬로 정렬 
valid.sort() 

for subset in valid:
    print(*subset)
    