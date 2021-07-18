#include<iostream>
#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  double x,y,z,w;
  cin >> x >> y >> z >> w;
  //Brahmaguptas
  double s = (x+y+z+w)/2;
  cout << setprecision(10) << sqrt((s-x)*(s-y)*(s-z)*(s-w)) << endl;
}
