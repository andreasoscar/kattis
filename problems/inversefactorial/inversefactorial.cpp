#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string n;
  cin >> n;
  if(n.size() < 7 && std::stoi(n) < 7){
    int fac = 1;
    map<long,long> m;
    for(int i = 1; i < 7; ++i){
      fac = fac*i;
      m[fac] = i;
    }
    cout << m[std::stoi(n)] << endl;
  } else {
    double res = 0;
    for(int i=1; i <= 1000000; ++i){
      res += log10(i);
      if((int)res + 1 == n.size()){
        cout << i << endl;
        break;
      }
    }
  }
}
