#include <iostream>
using namespace std;

int main() {
  int n, m;
  while (cin >> n >> m) {
    double p = (double) n / (n + m);
    printf("%.5f\n", p);
  }
}
