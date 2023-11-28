#icpc나간 동기의 조언을 받아 작성하였음
import math

n = int(input())
s = input().strip().split()
stack = []

for q in s:
    try:
        q = int(q)
        stack.append([q,1])
    except:
        stack.append(q)
    if len(stack) >4:
        if stack[-5] == '(' and type(stack[-4]) == type(stack[-3]) == type(stack[-2]) == list and stack[-1] == ')':
            numerator_a, denominator_a = stack[-4]
            numerator_b, denominator_b = stack[-3]
            numerator_c, denominator_c = stack[-2]
            numerator = numerator_a * denominator_b * numerator_c + denominator_a * numerator_b * denominator_c
            denominator = denominator_a * denominator_b * numerator_c
            for _ in range(5):stack.pop()
            num = math.gcd(numerator,denominator)
            stack.append([numerator//num, denominator//num])

            
if len(stack) == 1 and type(stack[0]) == list:
    print(*stack[0])
else:
    print(-1)