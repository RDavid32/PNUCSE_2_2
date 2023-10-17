n = int(input())
yard = [[] for _ in range(n)]
check_len = [0 for _ in range(n)]
for q in range(n):
    arr= list(map(int,input().split()))
    if arr[0]:
        yard[q] = arr[1:]
        check_len[q] = len(arr) -1
    else:
        check_len[q] = 0

min_len = min(check_len)
max_len = max(check_len)
while min_len+1 < max_len:
    max_index = [i for i in range(n) if check_len[i] == max_len]
    if len(max_index) >= 2:
        max_index = [max((yard[q][-1],q) for q in max_index )[1]]
    min_index = check_len.index(min_len)
    yard[min_index].append(yard[max_index[0]].pop(-1))
    check_len[min_index] += 1
    check_len[max_index[0]] -= 1
    min_len = min(check_len)
    max_len = max(check_len)

for q in yard:
    print(*q)