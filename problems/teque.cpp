#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  std::vector<int> first;
  std::vector<int> last;
  int n;
  string s;
  int n1;
  cin >> n;
  while(n > 0){
    cin >> s >> n1;
    if(s == "push_back"){
      last.push_back(n1);
    } else if(s == "push_front"){
        first.insert(first.begin(),n1);
    } else if(s == "push_middle"){
        if(first.size() == last.size()){
            first.insert(first.end(),n1);
        } else if(first.size() >= last.size()){
            last.insert(last.begin(),n1);
            //3,5,9 -> 3,5,1,9 -> 3,5,2500,1,9 -> 3,5,2500,1,9,9999 -> 3,5,2500,1,9,9999,250 -> -1,3,5,2500,25000,1,9,9999,250 ->  
        }
    } else if(s=="get"){
      if(n1 < first.size()){
        cout << first[n1] << endl;
      } else if(n1 >= first.size() and n1 <(first.size() + last.size())){
        cout << last[n1-first.size()] << endl;
      }
    }
    n -= 1;
  }
}