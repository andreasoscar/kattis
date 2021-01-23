#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <map>
#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  int a;
  int b;
  string h;
  cin >> n;
  map<int,string> k;
  map<int,string> c;
  for(int i = 0; i < n; i++){
    cin >> h;
    k[i] = h;
    c[i] = "";
  }
  for(int i=0; i < n-1;i++){
    cin >> a >> b;
    c[a-1] += to_string(b-1);
  }
  for(int i = 0; i < c.size();i++){
    cout << c[i] << endl;
  }
}
