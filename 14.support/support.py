from queue import PriorityQueue
import math

class support:
    def __init__(self, start, idx, time):
        self.start = start
        self.idx = idx
        self.time = time


    def __lt__(self, other):
        return self.time > other.time if self.time != other.time else self.start < other.start

    
n = int(input())
que =  PriorityQueue()
arr = [support(*map(int,input().split())) for _ in range(n)]

current_time = 30
idx = 0


def consultation_append(que,arr,current_time):
    while arr and arr[0].start < current_time:
        que.put(arr[0])
        del arr[0]

    if arr and que.empty():
        que.put(arr[0])
        current_time = arr[0].start
        del arr[0]
        

while  arr or not que.empty():
    consultation_append(que, arr, current_time) 
    
    people = que.get()

    if people.time <= 10:
        current_time += people.time
        print(people.idx)
        
    else:
        people.start = current_time + people.time
        current_time += math.floor(people.time/2)
        people.time = math.ceil(people.time/2)
                
        index_to_insert_at = None
        for i, existing_support in enumerate(arr):
            if people.start < existing_support.start:
                index_to_insert_at = i
                break

        if index_to_insert_at == None:
            index_to_insert_at = len(arr)

        arr.insert(index_to_insert_at, people)
        