#include <deque>
#include <iostream>
#include <list>
#include <string>
#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  std::deque<int> first;
  std::deque<int> last;
  int n;
  string s;
  int n1;
  cin >> n;
  while(n > 0){
    cin >> s >> n1;
    if(s == "push_back"){
      last.push_back(n1);
      if(last.size() > first.size()){
        first.push_back(last.front());
        last.pop_front();
      }
    
    } else if(s == "push_front"){
      first.push_front(n1);
      if(first.size() > (last.size() + 1)){
        last.push_front(first.back());
        first.pop_back();
      }
    } else if(s == "push_middle"){
      if(first.size() > last.size()){
        last.push_front(n1);
      } else {
        first.push_back(n1);
      }
    } else if(s=="get"){
      if(n1 < first.size()){
        cout << first[n1] << endl;
      } else if(n1 >= first.size() && n1 <= (first.size()+last.size())){
        cout << last[n1-first.size()] << endl;
      }
    }
    n -= 1;
  }
}