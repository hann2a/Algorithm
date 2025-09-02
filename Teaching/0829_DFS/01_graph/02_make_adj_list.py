import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 리스트) ---
V, E = map(int, input().split())

# 간선 정보를 리스트 하나로 입력 받기 
edge_data =  list(map(int, input().split()))


# --- 결과 확인 ---
