from queue import PriorityQueue
import math

class support:
    def __init__(self, start, idx, time, check):
        self.start = start
        self.idx = idx
        self.time = time
        self.check = check

    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time
        elif self.check != other.check:
            return self.start < other.start
    
n = int(input())
que =  PriorityQueue()
arr = [support(*map(int,input().split()),_) for _ in range(n)]
arr.sort(key=lambda x: x.start)

current_time = 30
count = n

for person in arr:
    que.put(person)
    
while not que.empty():
    person = que.get()

    if person.start > current_time:
        current_time = person.start

    if person.time <= 10:
        current_time += person.time
        print(person.idx)
    else:
        current_time += math.floor(person.time/2)
        person.time = math.ceil(person.time/2)
        count += 1
        person.check = count
        que.put(person)
