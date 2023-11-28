from collections import deque
def bfs(start):
    visited = set()
    queue = deque([(start,0)])
    visited.add(start)
    result = {}
    while queue:
        current_node, depth = queue.popleft()
        result[current_node] = depth
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                visited.add(neighbor)
                
    return result
    
n = int(input())

three_friend = list(input().split())

graph = {}
check = []
for _ in range(n):
    vertax, *adjacent_vertex, _ = input().split()
    graph[vertax] = adjacent_vertex


for q in three_friend:
    check.append(bfs(q))

common_key =  set(check[0]) & set(check[1]) & set(check[2])
result_dict = {key: max(check[0].get(key, 0), check[1].get(key, 0), check[2].get(key, 0)) for key in common_key}

if result_dict:

    min_value_key, min_value = sorted(result_dict.items(), key=lambda x : (x[1],x[0]))[0]

    print(min_value_key)
    print(min_value * 3 - 2)
    
else:
    print("@")
    print(-1)