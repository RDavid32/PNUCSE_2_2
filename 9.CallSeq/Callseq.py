from collections import deque

def CallSeq(visited, queue, name):
    if name in visited:
        print("DEADLOCK")
        exit()
    visited.append(name)
    for value in statements[name]:
        if value.isupper():
            CallSeq(visited, queue, value)
        else:
            queue.append([name,value])
    visited.pop()

def result (num):
    if 0 < num <= scope:
        print(f"{queue[num-1][0]}-{queue[num-1][1]}")
    elif -scope <= num <= scope:
        print(f"{queue[num][0]}-{queue[num][1]}")
    else:
        print("NONE")

N, k1, k2 = map(int,input().split())

queue = deque([])
statements = {}
visited = []

for q in range(N):
    fuction_name, *check, _ = input().split()
    statements[fuction_name] = check

CallSeq(visited, queue, "M")
scope = len(queue)
result(k1)
result(k2)