import sys
input = sys.stdin.readline

n = int(input())
money_list = []
result = "NONE"

for q in range(n):
    a,b = input().split()
    money_list.append([a,int(b)])
money_list.sort(key = lambda x : x[1], reverse=True)
max_money = money_list[0][1]
result = money_list[0][0]
check = 0

for q in money_list[1:]:
    if q[1] == max_money:
        check = 1
    elif q[1] < max_money:
        if check == 0:
            print(result)
            exit()
        max_money = q[1]
        check = 0
    result = q[0]

print("NONE")
