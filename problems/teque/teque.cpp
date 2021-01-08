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
  int mid = -1;
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
      if(mid > 0){
        if(first.size() == last.size()){
          last.insert(last.begin()+1,mid);
          cout << "w";
          mid = n1;
        } else if(last.size() > first.size()){
          first.push_back(mid);
          cout << "a";
          mid = n1;
        } else if(first.size() > last.size()){
          last.insert(last.begin(),mid);
          cout << "k";
          mid = n1;
        }
      } else {
        mid = n1;
      }
       //3,5,9 -> 3,5,1,9
    } else if(s=="get"){
      int total = first.size() + last.size();
      for (auto i = first.begin(); i != first.end(); ++i)
        std::cout << *i << " ";
      std::cout << mid << " ";
      for (auto i = last.begin(); i != last.end(); ++i)
        std::cout << *i << " ";
      std::cout << endl;
      if(n1 == total/2){
        //cout << mid << endl;
      } else if(n1 < total/2){
        //cout << first[n1] << endl;
      } else if(n1 > total/2){
        //cout << last[n1-first.size()-1] << endl;
      }
    }
    n -= 1;
  }
}
