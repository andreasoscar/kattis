#include <vector>
#include <iostream>
#include <math.h>
using namespace std;
int main() {
  int n,q;
  //http://www.cplusplus.com/doc/tutorial/basic_io/, how to read in with cin
  cin >> n >> q;
  //https://www.cplusplus.com/reference/vector/vector-bool/
  vector<bool> p(n+1,true);
  p[0] = false;
  p[1] = false;
  //standard sieve algorithm
  for (int j = 2; j <= sqrt(n);j++){
    if(p[j]){
      for (int k = j*j; k <= n;k+=j){
        p[k] = false;
      }
    }
  }
  //check how many numbers less than n is prime
  int x = 0;
  for (int v = 0; v <= n;v++){
    if(p[v]){
      x++;
    }
  }
  //https://developerinsider.co/how-to-break-a-output-line-in-cpp/
  cout << x << endl;
  //go through input
  for(int s = 0; s < q;s++){
    int in;
    cin >> in;
    if(p[in]){
      cout << 1 << endl;
    } else {
      cout << 0 << endl;
    }
  }
}
