#include<iostream>
#include <string>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string word;
  std::cin >> word;
  for (int i = 0; i < 3; i++){
    std::cout << word << " ";
  }
  std::cout << endl;

}
