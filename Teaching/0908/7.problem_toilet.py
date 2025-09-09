time_list = [15, 30, 50, 10]

time_list.sort()

cumul_time = 0
wait_sum = 0

for time in time_list:
    wait_sum+= cumul_time
    cumul_time += time

print('총 대기시간', wait_sum)