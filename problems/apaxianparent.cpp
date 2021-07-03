#include<iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string a,b;
  cin >> a >> b;
  if(a.substr(a.length()-2) == "ex"){
      cout << a << b << endl;
  } else if(a.substr(a.length()-1) == "e"){
      cout << a << "x" << b << endl;
  } else if(a.substr(a.length()-1) == "a" || a.substr(a.length()-1) == "i" || a.substr(a.length()-1) == "o" || a.substr(a.length()-1) == "u"){
      cout << a.substr(0, a.length()-1) << "ex" << b << endl;
  } else {
      cout << a << "ex" << b << endl;
  }
}
