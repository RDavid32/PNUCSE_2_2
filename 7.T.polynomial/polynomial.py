n = int(input())
arr = {}
for _ in range(n):
    
    t = int(input())
    for q in range(t):
        i, e = map(int,input().split())
        if e in arr:
            arr[e] += i
            
        else:
            arr[e] = i
check = dict(sorted(arr.items(),reverse=True))

result = {key: value for key, value in check.items() if value != 0}
if result:
    print(len(result))
    for key, value in result.items():
        print(value, key)
else:
    print("0 0")