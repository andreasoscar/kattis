#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int k,v;
  vector<string> s;
  std::cin >> k;
  int expenses = 0;
  for (int i = 0; i < k; i++){
    std::cin >> v;
    if(v < 0){
      expenses -= int(v);
    }
  }
  std::cout << expenses << endl;
}
