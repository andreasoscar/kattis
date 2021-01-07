#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
using namespace std;
int main() {
  int i,j,h,total;
  cin >> i >> j;
  while (i && j != 0){
    std::unordered_set<int> jack;
    int total = 0;
    for(int k=0;k < i;k++){
      cin >> h;
      jack.insert(h);
    }
    for(int k=0;k < j;k++){
      cin >> h;
      if(jack.count(h)){
        total++;
      }
    }
    cout << total << endl;
    cin >> i >> j;
  }
}
