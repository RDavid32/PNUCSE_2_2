N, K = map(int,input().split())
shopping = [0 for _ in range(K)]
arr = [list(map(int,input().split())) for _ in range(N)]
index = 0
while True:
    check = 1
    for shopping_idx, time in enumerate(shopping):
        if not time:
            shopping[shopping_idx] = arr[]
            check = 0