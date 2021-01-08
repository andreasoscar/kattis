#include <vector>
#include <sstream>
#include <iostream>
#include <list>
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin >> n;
  list<string> teque;
  string s;
  getline(cin, s);
  for(int i = 0; i < n;i++){
    getline(cin, s);
    istringstream s2(s);
    vector<string> v;
    string tmp;
    while (s2 >> tmp) {
      v.push_back(tmp);
    }
  if(v.front() == "push_back"){
    teque.push_back(v.back());

  } else if (v.front() == "push_front"){
    teque.push_front(v.back());

  } else if (v.front() == "push_middle"){
    std::list<string>::iterator it = teque.begin();
    std::advance(it, (1+teque.size())/2);
    teque.insert(it, v.back());
  } else if (v.front() == "get"){
    vector<string> vec(teque.begin(), teque.end());
    cout << vec[std::stoi(v.back())] << endl;

  }
 }
}
