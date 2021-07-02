#include<iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string t;
  cin >> t;
  bool check = false;
  for (int i = 0; i < t.length(); i++){
      for (int j = 0; j < t.length(); j++){
          if(i != j){
              if (t[i] == t[j]){
                  check = true;
                  break;
              }
          }
      }
  }
  if(!check){
      cout << "1";
  } else {
      cout << "0";
  }
}
