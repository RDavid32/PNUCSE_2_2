#--------------------------------------------------------
# Author:      Zoh Que
# Created:     19-10-2023
#--------------------------------------------------------
import random

L1 = [ 3, -8, 1, 6, 10, 7, 2, 2, 9  ] 
L2 = [ 7, 3, -8, 1, 6, 1, 4, 10, 7, 2, 10, 2, 9  ] 
L3 = [ 3, 2, 1, 10, 7, 3, -8, 1, 6, 1, 4, 10, 7, 2, 10, 2, 9  ] 



# 이것을 완성해야 합니다.
def GetM(i, j, myL) :
    n = (len(myL)+1) /2
    if i > n or j > n: #범위 벗어나면 0 출력
        return 0
    if i == j: 
        return(myL[2 * i -2])
    if i + j == n + 1:
        if i > n // 2: #myL[n//2][n//2]가 중복되어서 예외처리
            return(myL[2 * (i-1) - 1])
        return(myL[2 * i - 1])
    return 0
    



def Mtest( myL ):
    n = (len(myL)+1) /2

    for w in range( int(n*n/2) ):
        i = random.randint(1,n+1)
        j = random.randint(1,n+1)
        value = GetM(i,j, myL )
        print(f" {i=}, {j=}, {value=}")


print(f"\n L1 ")
Mtest(L1)

print(f"\n L2 ")
Mtest(L2)

print(f"\n L3 ")
Mtest(L3)