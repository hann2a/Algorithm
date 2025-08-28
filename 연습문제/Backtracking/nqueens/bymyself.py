def solve_nqueens(n):
    solutions = []
    queens = [-1] * n
    backtrack_nqueens(n, 0, queens, solutions)
    return solutions

def backtrack_nqueens(n, row, queens, solutions):
    if row == n:
        solutions.append(queens[:])
        return 
    
    for col in range(n):
        if can_place(queens, row, col):
            queens[row] = col
            backtrack_nqueens(n, row+1, queens, solutions)

def can_place(queens, new_row, new_col):
    for r in range(new_row):
        c = queens[r]
        if c == new_col:
            return False
        if abs(new_row - r) == abs(new_col - c):
            return False
    return True 

n = 4
results = solve_nqueens(n)
print(f"N={n}일 때, 가능한 해의 개수:", len(results))
for sol in results:
    print(sol)


