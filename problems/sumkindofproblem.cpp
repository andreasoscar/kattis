#include<iostream>
#include <string>
using namespace std;

int main() {
  int number;
  std::cin >> number;
  for(int i = 0; i < number; i++){
    int k = 0;
    int n = 0;
    int sum = 0;
    int oddSum = 0;
    std::cin >> k >> n;
    for(int i = 1; i <= n; i++){
      sum += i;
    }
    for(int i = 1; i <= 2*n; i += 2){
      oddSum += i;
    }
    string complete = to_string(k) + " " + to_string(sum) + " " + to_string(oddSum) + " " + to_string(oddSum+n);
    std::cout << complete << endl;
  }
}
