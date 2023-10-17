def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] <= target < data[mid+1]:
            return mid 
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

N, K = map(int,input().split())
max_seat = 2*K
arr = {}
result = []
for _ in range(N):
    symbol, num = input().split()
    num = int(num)
    if symbol == "+":
        if result:
            if num < result[0]:
                arr[num] = arr.pop(result[0])
                result[0] = num
                check = num    
                
            else: 
                if result[-1] <= num:
                    check = result[-1]
                else: 
                    check = result[binary_search(num, result)]
            arr[check].append(num)
            arr[check].sort()
            if len(arr[check]) == max_seat:
                result.insert(check,arr[check][K])
                arr[arr[check][K]] = arr[check][K:]
                arr[check] = arr[check][:K]
                result.sort()
        else:
            result.append(num)
            arr[num] = [num]
            
    else:
        if num < result[0]:
            continue
        else:
            if result[-1] <= num:
                check = result[-1]
            else: 
                check = result[binary_search(num, result)]

            if num in arr[check]:
                
                idx = arr[check].index(num)
                
                arr[check].remove(num)
                
                if idx ==0:
                    if arr[check]:
                        new_num =arr[check][0]
                        result[result.index(num)] = new_num
                        arr[new_num] = arr.pop(num)
                    else:
                        result.remove(num)

    
for q in result:
    print(q)