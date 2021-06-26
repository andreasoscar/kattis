#include<iostream>
#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  double miles;
  std::cin >> miles;
  int converted = miles * (5280.0/4854.0) * 1000.0 + 0.5;
  std::cout << converted << endl;
}
