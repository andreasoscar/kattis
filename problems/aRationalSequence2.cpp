#include<iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;


int compute(int p, int q){
    if(p == q){
        return 1;
    }

    if(p > q){
        return 2*compute(p-q, q)+1;
    }

    if(p < q){
        return 2*compute(p,q-p);
    }
}

int main() {
  std::vector<std::string> ratios;
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n = 0;
  std::cin >> n;
  
  for(int i = 0; i < n; ++i){
      std::string read;
      int d = 0;
      std::cin >> d >> read;
      ratios.push_back(read);
  }

  for(int i = 1; i <= n; ++i){
      std::istringstream iss(ratios[i-1]);
      std::string p_, q_;

      std::getline(iss, p_, '/');
      std::getline(iss, q_);

      int p = std::stoi(p_);
      int q = std::stoi(q_);
      
      int newN = compute(p,q);
      std::cout << i << " " << newN << std::endl;
  }
}

