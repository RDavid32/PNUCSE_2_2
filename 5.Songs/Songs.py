N, k =map(int,input().split())
result = 1
arr =[]
for _ in range(N):
    T, G, B, S, D = input().split()
    arr.append([T,G,int(B),float(S),int(D)])
    
arr.sort(key=lambda x: (-x[2], -x[4], x[3]))
check_gerne = arr[0][1]
visit = [0 for _ in range(N)]
visit[0] = result

while True:
    flag =False
    for idx, q in enumerate(arr):
        if flag:
            break
        if check_gerne != q[1] and not visit[idx]:
            flag = True
            result+=1
            if result == k:

                print(q[0])
                exit()
            visit[idx] = result
            check_gerne = q[1]