#--------------------------------------------------------
# Author:      Zoh Que
# Created:     18-10-2023
#--------------------------------------------------------

# 이 함수를 채우시오.
def Xrotate(X) :
    if not X: #예외처리
        return X
    chage_T = X[:]
    chage_T[-1].append(X[0][0]) #마지막에 추가 
    for q in range(len(X)-1): #처음 값은 지우고 마지막 값은 추가
        del chage_T[q][0]
        chage_T[q].append(X[q+1][0])

    del chage_T[-1][0] #마지막 제외 (범위 예외처리)
    
    return chage_T


def showvv( X ) :
    for Vr in X :
        print("\n > ", end="")
        for w in Vr :
            print(f" {w}", end="")

T =  [ [21], [54,30,2], [17,9], [50],
        [4,62,99,21], [16,20], [9,5,54] ]

Xrotate(T)
showvv(T)