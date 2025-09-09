arr = ['A','B', 'C', 'D', 'E']

# 최소 두 명 이상의 친구
result = []
for i in range(1 << len(arr)):
    now_result = []   # i 루프가 시작할 때 초기화
    for idx in range(len(arr)):
        if i & (1 << idx):
            now_result.append(arr[idx])   # 포함되는 원소 모으기

    if len(now_result) >= 2:
        result.append((now_result, i))    # 튜플로 저장

print(result)   # 루프 다 끝난 후 최종 출력
