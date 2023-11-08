#--------------------------------------------------------
# Author:      Zoh Que
# Created:     19-10-2023
#--------------------------------------------------------

stack = [ 6, 7, 12, 3, 34, 34, 3, 10, 10, 10, 3, 51, 33, 33, 41 ]

def Pstack( msg, S ):
    print(f"\n {msg}: ")
    for w in S :
        print(f" > {w}")

def squiz( mystack):
    mystack.append(-1)
    count = 1

    while count: #한번씩 될 수 있게 확인
        check = 0
        count =0
        idx = 0
        check_num = -1
        while mystack[idx] != -1: #마지막 값이 될때까지 봄
            if check_num == mystack[idx]: 
                del mystack[idx] #중복되면 지움
                count += 1
                if check: #중복된게 처음 나올때를 위한 예외처리
                    idx -=1
                    del mystack[idx]
            else:
                check_num = mystack[idx] #같지 않으면 다음 칸과 check 변환
                idx += 1
                check = 1
    del mystack[-1]
    return mystack
            






Pstack("> 처음상태 ", stack)

squiz( stack )

Pstack("> 바뀐 상태 ", stack)
