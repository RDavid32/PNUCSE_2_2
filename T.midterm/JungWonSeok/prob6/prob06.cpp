// vector에서 적용할 수 있는 다양한 동작(operator) 중 sorting을 실험해 봄

#include <bits/stdc++.h>
#define allout(MSG,X)   std::cout<<"\n"<<MSG <<" : ";for(auto w:X)std::cout<<w<<", "
using namespace std;

// 여러분은 이 함수를 완성해야 합니다.
vector<int> Tomato( vector<int> myv ){
    vector<int> yourv ;
    yourv = myv ;
    yourv.pop_back() ;
    return ( yourv ) ;

}


int main() {

    vector<int> Box { 1, 2, 3, 1, 2, 3, 5, 6, 5, 6, 10 } ;
//  vector<int> Box { 9, 8, 11, 2, 3, 5, 45, 21, 32, 11, 45, 45, 8, 13 } ;
//  vector<int> Box { 7,7,7,7,7,7,7,7 } ;

    allout(" 작업 전 Box[]", Box ) ;

    auto Apple = Tomato( Box ) ;

    allout(" 작업 후 Apple[]", Apple ) ;


} // end of main ( )
