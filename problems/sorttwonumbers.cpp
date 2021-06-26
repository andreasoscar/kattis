#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int k,n;
  std::cin >> k >> n;
  if(k<n){
    std::cout << k << " " << n << endl;
  }
  else {
    std::cout << n << " " << k << endl;
  }
}
