#include<bits/stdc++.h>
#define MAX 1000
using namespace std;


template <typename T>
void ShowStack(std::stack<T> mystack) {
  std::cout <<"\n Stack Top: " ;
  if ( mystack.empty() ) cout << "��.. ����ִ� stack!" ;
  while (!mystack.empty()) {
    T top = mystack.top();
    mystack.pop();
    std::cout << top << " ";
  }
}

stack<int> Ready_stack(){
    vector<int> num {6, 7, 12, 3, 34, 34, 3, 10, 10, 10, 3, 51, 33, 33, 41};
    stack <int> banana ;
    for(auto w : num ) banana.push(w) ;
    return( banana) ;
}

// �� �Լ��� ä��ÿ�.
void Squiz( stack<int> &X ) {
    X.pop() ;
    X.push(999) ;
}

int main() {
    stack<int> mango;

    mango = Ready_stack() ;
    ShowStack(mango) ;

    Squiz( mango ) ;
    ShowStack(mango) ;
    return 0;
}  // end of main( )
