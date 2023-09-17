K = 0                      
check1, check2 = 0, 0            
cycle_time = 0             
dx = [1, -1, 0, 0]         
dy = [0, 0, 1, -1]     
graph = []              
sum_time = []       
direction = []            

def check_gap(x, y):
    if x > 0:
        return 0
    if x < 0:
        return 1
    if y > 0:
        return 2
    if y < 0:
        return 3
    return -1



def result(t):
    t %= cycle_time
    
    for idx in range(K):
        
        if sum_time[idx + 1] <= t:
            continue
        
        gap_time = t - sum_time[idx]
        nx = graph[idx][0] + (dx[direction[idx]] * gap_time)
        ny = graph[idx][1] + (dy[direction[idx]] * gap_time)
        return nx,ny
        

K = int(input())
for q in range(K):
    x, y = map(int, input().split())
    graph.append([x, y])
    
graph.append([graph[0][0], graph[0][1]])
sum_time.append(0)

for q in range(K):
    gap_x = graph[q + 1][0] - graph[q][0]
    gap_y = graph[q + 1][1] - graph[q][1]
    time = abs(gap_x + gap_y)
    
    if q + 1 == K // 2:
        check2 = cycle_time
    
    cycle_time += time
    sum_time.append(cycle_time)
    direction.append(check_gap(gap_x, gap_y))



t = int(input())
time1, time2 = check1, check2
s1, s2 = check1, check2

time1 = t % cycle_time
time2 = (cycle_time + time2 - time1) % cycle_time
if min(abs(s1 - time1), abs(cycle_time - time1)) < abs(s2 - time1):
    check1, check2 = time1, time2

else:
    check2, check1 = time1, time2

print(*result(check1))
print(*result(check2))