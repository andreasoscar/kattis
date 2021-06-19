#include <iostream>
int add(int c, int d){
  return c+d;
}
int main(){
  int a,b;
  std::cin >> a >> b;
  int sum = add(a,b);
  std::cout << sum;
  return 0;
}
