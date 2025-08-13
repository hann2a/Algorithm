import sys

sys.stdin = open('input.txt', 'r')

def until_last_long(arr, start_point):

        x, y = 0, start_point

        count_long = 0 

        while x < 99:
            if y-1 >= 0 and arr[x][y-1] == 1:
                while y -1 >= 0  and arr[x][y-1] == 1:
                    y -= 1
                    count_long += 1
            
            elif y + 1 < 100 and arr[x][y+1] == 1:
                while y + 1 < 100 and arr[x][y+1] ==1:
                    y += 1
                    count_long += 1                    
                
            x += 1
    
        return count_long 
        
T = 10

for t in range(1, 1+T):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    shortest_dis = float('inf')
    result_y = 0 

    for y_point in range(100):
         if arr[0][y_point] == 1:
              now_distance = until_last_long(arr, y_point)
              if now_distance < shortest_dis:
                   shortest_dis = now_distance
                   result_y = y_point
    
    print(f'#{t} {result_y}')