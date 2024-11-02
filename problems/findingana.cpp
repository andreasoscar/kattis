#include<iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string inp;
  cin >> inp;
  string::iterator it = find(inp.begin(), inp.end(), 'a');
  if(it != inp.end()){
    cout << string(it, inp.end()) << "\n";
  }
  return 0;
}



