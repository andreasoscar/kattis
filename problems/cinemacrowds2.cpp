#include<iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n,m;
  cin >> n >> m;
  string s;
  getline(cin, s);
  getline(cin, s);
  vector<int> groups;
  stringstream ss(s);
  while(getline(ss, s, ' ')){
    groups.push_back(stoi(s));
  }

  int index = 0;
  int sum = 0;
  for(int i = 0; i < groups.size(); i++) {
    if(sum+groups[index] <= n){
        sum += groups[index];
       
        index++;
    }
  }

  
  cout << (m-index) << "\n";
}
