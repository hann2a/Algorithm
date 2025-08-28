# solve_nqueens
# 입력: n
# 출력: solutions 
# queens를 초기화해서 갖고 있음 
# n, 첫째행, 초기화된 queens, 빈 solutions 값을 정함 
def solve_nqueens(n):
    solutions = []
    queens = [-1]*n
    backtrack_nqueens(n, 0, queens, solutions)
    return solutions

# backtrack_nqueens
# 입력: N, 현재 행, 퀸 정보가 있는 리스트, solutions
def backtrack_nqueens(n, row, queens, solutions):
    # 만약 행이 끝까지 갔으면 solutions에 지금까지 만든 queens를
    # 복사해서 append 
    if row == n:
        solutions.append(queens[:])
        return 
    
    # 행을 입력받았고, 따라서 열을 돌아다니면서 가능한지 확인 
    # 가능하면 queens 업데이트 
    for col in range(n): 
        if can_place(queens, row, col):
            queens[row] = col
            backtrack_nqueens(n, row+1, queens, solutions)

# can_place
# 입력: queens 리스트, 새 행, 새 열 
# 출력: Boolean(True, False)
def can_place(queens, new_row, new_col):
    # 그 때까지의 행중에 퀸이 같은 열에 놓여있는지 
    for r in range(new_row):
        c = queens[r]
        if c == new_col:
            return False
        if abs(new_row - r) == abs(new_col-c):
            return False 
    return True 

n = 4
results = solve_nqueens(n)
print(f"N={n}일 때, 가능한 해의 개수:", len(results))
for sol in results:
    print(sol)