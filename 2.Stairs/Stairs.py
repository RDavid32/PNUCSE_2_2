n = list(map(int,input().split()))

stairs = [0 for _ in range(1001)]
check = 0
x_coordinate = [i for i in n[::2]]
y_coordinate = [i for i in n[1::2]]

max_num = sum(y_coordinate)

sum_x_value = 0
x_prefix_sum = []

sum_y_value = max_num
y_prefix_sum = [max_num]

for i in range(len(y_coordinate)):
    sum_x_value += x_coordinate[i]
    sum_y_value -= y_coordinate[i]
    x_prefix_sum.append(sum_x_value)
    y_prefix_sum.append(sum_y_value)
    
x_prefix_sum.append(x_prefix_sum[-1])

while True:
    try:
        check = 0
        x, y = map(int,input().split())
        for idx, num in enumerate(x_prefix_sum):
            if x <= num:

                if y <= y_prefix_sum[idx] :
                    if (x == num and y >= y_prefix_sum[idx+1]) or (y == y_prefix_sum[idx] and x <= x_prefix_sum[idx+1]):
                        check = 2
                        break
                    check = 1
    
                break
        if check == 1:
            print('in')
        elif check == 2:
            print('on')
        else:
            print('out')
                
    except:
        break