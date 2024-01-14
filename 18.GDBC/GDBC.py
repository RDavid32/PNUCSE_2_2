import sys
input = sys.stdin.readline

registration = {}

while True:
    command, *gdbc = input().split()
    
    if command == "$":
        break
    
    target_frozenset = frozenset(map(int, gdbc[:-1]))

    if command == "R":
        registration.setdefault(target_frozenset, []).append(int(gdbc[-1]))
    else:
        print(" ".join(map(str, sorted(registration.get(target_frozenset, [None]), reverse=True))))
