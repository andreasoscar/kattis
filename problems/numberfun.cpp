#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int x;
  cin >> x;
  for(int i=0; i<x; i++){
    double y,z,q;
    cin >> y >> z >> q;
    if(y+z==q || y*z==q || y/z==q || y-z==q || z/y==q || z-y==q){
      cout << "Possible" << "\n";
    } else {
      cout << "Impossible" << "\n";
    }
  }
}
