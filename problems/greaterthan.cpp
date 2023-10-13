#include<iostream>
#include <string>
using namespace std;

int main() {
 // ios_base::sync_with_stdio(false);
 // cin.tie(NULL);
  int a = 0;
  int b = 0;
  std::cin >> a >> b;
  if(a > b){
    std::cout << "1" << std::endl;
  }
  else {
    std::cout << "0" << std::endl;
  }
}
