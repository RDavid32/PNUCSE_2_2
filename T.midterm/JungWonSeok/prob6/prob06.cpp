// vector���� ������ �� �ִ� �پ��� ����(operator) �� sorting�� ������ ��

#include <bits/stdc++.h>
#define allout(MSG,X)   std::cout<<"\n"<<MSG <<" : ";for(auto w:X)std::cout<<w<<", "
using namespace std;

// �������� �� �Լ��� �ϼ��ؾ� �մϴ�.
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

    allout(" �۾� �� Box[]", Box ) ;

    auto Apple = Tomato( Box ) ;

    allout(" �۾� �� Apple[]", Apple ) ;


} // end of main ( )
