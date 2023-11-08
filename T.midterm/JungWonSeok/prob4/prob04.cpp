#include <bits/stdc++.h>
using namespace std;

template <typename T>
void PrintQ(string MSG, queue<T> myQ) {
  std::cout <<"\n" << MSG << "\n " ;
  if ( myQ.empty() ) cout << "��.. ����ִ� Queue!" ;
  while (!myQ.empty()) {
    T top = myQ.front();
    myQ.pop();
    std::cout << top << "\n ";
  }
}


// �� �Լ��� �ϼ��ϼ���.
queue<int> Rearrange( queue<int> B ){
    queue<int> NewJul ;

    NewJul.push( B.front());
    NewJul.push( B.back() );
    NewJul.push( 12999    );
    return( NewJul ) ;
}

int main() {

   deque<int>  Order \
   {153, 213, 134, 156, 170, 250, 233, 204, 167, 281, 266, 133, 199, 178} ;

   queue<int, deque<int>> Build6 ( Order ) ;
   queue<int>  NewJul ;    // ���� ��ģ ��

   PrintQ( " 1. Build6[]= ", Build6 );

   NewJul = Rearrange( Build6 ) ;

   PrintQ( " 2. Newjul[]= ", NewJul );

}
