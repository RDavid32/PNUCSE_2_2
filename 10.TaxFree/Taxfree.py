def find_best_coupon_combination(N, K, arr):
    best_combination = []

    def find_combination(current_combination, current_total_price, start_index):
        nonlocal best_combination

        if current_total_price == K:
            best_combination = max(best_combination,current_combination)[:]
            
            return
        
        if current_total_price > K:
            return
        
        for i in range(start_index, N):
            current_combination.append(arr[i])
            find_combination(current_combination, current_total_price + arr[i], i + 1)
            current_combination.pop()

    find_combination([], 0, 0)
    return best_combination

N, K = map(int, input().split())
prices = [int(input()) for _ in range(N)]

arr = sorted(prices, reverse=True)

check = find_best_coupon_combination(N, K, arr)
if check:
    for q in sorted(check):
        print(q)
else:
    print(0)