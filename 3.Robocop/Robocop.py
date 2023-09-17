import sys
input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
time = [0 for _ in range(n+1)]

start_x ,start_y = map(int,input().split())
graph[0] = [start_x,start_y]
check_x, check_y = start_x, start_y
time_sum = 0

for q in range(1,n):
    x, y = map(int,input().split())
    graph[q] = [x,y]
    time_sum += abs(check_x-x) + abs(check_y - y)
    time[q] = time_sum
    check_x, check_y = x, y
    
graph[n] = [start_x,start_y]
time_sum += abs(start_x-x) + abs(start_y - y)
time[n] = time_sum

t = list(map(int,input().split()))
for q in t:
    check_time = q % time_sum

    for idx, value in enumerate(time):

        if value > check_time:
            start_point = idx
            break
    start_point-=1
    subtract_time =time[start_point] - check_time 

    direction_x = graph[start_point][0] - graph[start_point+1][0]
    direction_y = graph[start_point][1] - graph[start_point+1][1]

    if direction_x < 0:
        print(graph[start_point][0] - subtract_time, graph[start_point][1])
    elif direction_x > 0:
        print(graph[start_point][0] + subtract_time, graph[start_point][1])
    else:
        if direction_y < 0:
            print(graph[start_point][0] , graph[start_point][1] - subtract_time)
        elif direction_y >0:
            print(x)
