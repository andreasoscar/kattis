#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
 #include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string s;
  string fs;
  while(true){
    getline(cin,s);
    getline(cin,fs);
    if(cin.eof()){
      return 0;
    }
    int f = fs.find(s);
    std::vector<int> v;
    while(f != std::string::npos){
      v.push_back(f);
      f = fs.find(s,f+1);
    }
    for(int i = 0; i < v.size();i++){
      cout << v[i] << " ";
    }
    cout << endl;
    }
  }
