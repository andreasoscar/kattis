#include<iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main() {
  double in;
  std::cin >> in;
  std::cout << std::setprecision(15) << 4*sqrt(in) << endl;
}
