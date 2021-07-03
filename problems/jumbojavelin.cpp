#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int nbr;
  int sum = 0;
  cin >> nbr;
  for (int i = 0; i < nbr; i++){
      int v;
      cin >> v;
      sum += v;
  }
  sum -= (nbr-1); 
  cout << sum;
}
