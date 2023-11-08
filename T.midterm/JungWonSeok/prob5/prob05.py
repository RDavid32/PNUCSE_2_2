
mys = list("atttgcctgatttttacgaatcggggattag")
mys1 = list("atttgccgaatcggggattctgatttttaag")
mys2 = list("atgcaatgcaatgcaatgcaatgca")
mys3 = list("ttttttttaaaaaaaacccccccc") #  --> 처리 결과도 동일함.


# 이 함수롤 제대로 완성해야 합니다.

def make_dna( L ) :
    if not L:
        return ''
    L.append('$')
    T = []
    check = '$'
    count =0
    idx = 0
    start_idx = 0
    end_list = []
    while L[idx] != '$': #마지막을 만나면 종료됨
        if L[idx] == check:
            count += 1
        else:
            if count >= 2:
                end_list.append(L[start_idx:start_idx+count+1 ]) #중복된 리스트 추가
                count =0
            elif count == 1: #중복된게 2개까지 나왔으면 넣어야 하기에
                T.append(L[idx-1])
                T.append(L[idx-1])
            else: #처음에 예외처리를 위한 $가 들어가있음
                T.append(L[idx-1])
            check = L[idx]
            count = 0
            start_idx = idx
        idx+=1
    del T[0] #처음 $지워줌

    if count >= 2: #마지막에 넣기 위한 구문
        end_list.append(L[start_idx:start_idx+count+1 ])
    elif count == 1:
        T.append(L[-2])
        T.append(L[-2])
    else:
        T.append(L[-2])
    for q in end_list: #3개 이상 중복된 리스트 추가
        T += q
    return( T ) 



print( mys )

yours1 = make_dna( mys )
print( yours1 )
