data = {
    1: [5, 6, 3],
    2: [6, 9, 8],
    3: [5, 1, 4, 9],
    4: [8, 7, 3],
    5: [1, 3],
    6: [2, 8, 1],
    7: [9, 4],
    8: [6, 2, 4],
    9: [2, 3, 7]
}

if __name__ == "__main__":
    start_u, start_v = map(int,input().split())
    current_vertax = data[start_u][data[start_u].index(start_v)-1] #시계 방향으로 돌때
    past_vertax = start_u
    print(start_v, start_u, end = ' ')
    while current_vertax != start_v:
        print(current_vertax, end = ' ')
        check = current_vertax
        current_vertax = data[current_vertax][data[current_vertax].index(past_vertax)-1] #시계 방향으로 돌때
        past_vertax = check
    print()

    current_vertax = data[start_v][data[start_v].index(start_u)-1] #반시계 방향으로 돌때
    past_vertax = start_v
    print(start_u, start_v, end = ' ')
    while current_vertax != start_u:
        print(current_vertax, end = ' ')
        check = current_vertax
        current_vertax = data[current_vertax][data[current_vertax].index(past_vertax)-1] #반시계 방향으로 돌때
        past_vertax = check

