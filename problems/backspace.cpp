#include<iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <iterator>
using namespace std;

void modify(string& in){
  int remove = 0;
  for (int i = in.length() - 1; i >= 0; i--) {
    if(in[i] == '<'){
      in[i] = '_';
      remove++;
    }
    else if (remove > 0){
      in[i] = '_';
      remove--;
    }
  }
  string result;
  std::remove_copy(in.begin(), in.end(), std::back_inserter(result), '_');
  std::cout << result << endl;
}

int main() {
  string input;
  std::cin >> input;
  modify(input);
}
