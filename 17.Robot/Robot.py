def solution(N, turn_time, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]

    queue = [(N-1, 0, -1, 0)]  
    visited[N-1][0][-1] = 0

    while queue:
        x, y, current_direction, time = queue.pop(0)

        for q, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                new_time = time + 1 if q == current_direction or current_direction == -1 else time + turn_time + 1
                if new_time < visited[nx][ny][q]:
                    visited[nx][ny][q] = new_time
                    queue.append((nx, ny, q, new_time))
        
    result = min(visited[0][N-1])
    
    return result if result != float('inf') else -1

N, turn_time = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, turn_time, grid))