#include <vector>
#include <iostream>
#include <string>
#include <bits/stdc++.h>
#include <math.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  std::vector<int> pf;
  int n,m;
  cin >> n >> m;
  while(n%2 == 0){
      pf.push_back(2)
      n = n/2;
  }
  for(int k=3; k <= sqrt(n);k = k + 2){
      while(n%k == 0){
          pf.push_back(k);
      }
  }
  if(n>2){
      pf.push_back(n);
  }
  

}