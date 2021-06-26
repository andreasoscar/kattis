#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n,r;
  std::cin >> n >> r;
  int diff = n - r;
  double s = 0.0;
  for (int i = 0; i < r; i++){
    int tmp = 0.0;
    std::cin >> tmp;
    s += tmp;
  }
  double min,max;
  min = (s - 3.0*diff)/n;
  max = (s + 3.0*diff)/n;
  std::cout << min << " " << max << endl;
}
