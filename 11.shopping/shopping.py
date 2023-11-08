N, K = map(int,input().split())
shopping = [[] for _ in range(K)]
arr = [list(map(int,input().split())) for _ in range(N)]
index = 0
count = 0

while True:
    if count == 0 and index ==N:
        break
    if count < K and index != N:
        for shopping_idx, time in enumerate(shopping):
            if not time:
                shopping[shopping_idx] = arr[index]
                index += 1
                count += 1
            if count == K or index == N :
                break
    else:
        check =  min((row[1] if row else 21) for row in shopping)
        shopping = [[cart[0],cart[1]  - check] if cart else [21,21] for cart in shopping]
        for idx, q in enumerate(shopping[::-1]):
            if not q[1]:
                print(q[0])
                shopping[-idx-1] = []
                count -= 1