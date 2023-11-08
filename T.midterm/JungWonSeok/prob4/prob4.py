#--------------------------------------------------------
# Author:      Zoh QueFir
# Created:     19-10-2023
#--------------------------------------------------------

L1 = [ 153, 213, 134, 156, 170, 250, 233, 204, 167, 281, 266, 133, 199, 178 ]

def showQ( MSG, myL):
    print(f"\n Queue {MSG} - 출력하기 ")
    for w in myL :
        print(f">  {w}")

def Rearrange( inL ):
    check = 2
    myL = []
    index_list = [999,-1,-1] #위치 확인(0은 안쓰기에 999넣음)

    index = 0
    while index < len(inL):
        if inL[index] //100 == check:
            index_list[check] = index
            myL.append(inL[index]) #결과에 추가
            check = max((check+1)%3,1) #1 ->2 ,2->1로 가기 위한 구문 (앞자리 수 확인을 위한)
            index = index_list[check] + 1
        else:
            index += 1
    
    if index_list[2] < index_list[1]: #똑같은 성별을 추가하기 위해서 넣음
        for q in inL[index_list[1]+ 1:]: #이떄 인덱스의 가장 큰거 이후로 같은 값을 추가
            if q // 100 == 1:
                myL.append(q)
    else:
        for q in inL[index_list[2]+ 1:]:
            if q // 100 == 2:
                myL.append(q)


    return( myL)




NewJul = Rearrange(L1)
showQ( "처음 줄 ", L1)
showQ( "다시 정리된 줄 ", NewJul)