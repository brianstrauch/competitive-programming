#include <iostream>
using namespace std;

int n;
int a[100000];

int solve(int l, int r) {
  l--;
  r--;

  int sum = 0;
  for (int i = l; i <= r; i++) {
    int x = 0;
    for (int j = i; j <= r; j++) {
      x ^= a[j];
      sum = (sum + x) % 1000000007;
    }
  }
  return sum;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int q;
    cin >> n >> q;
    for (int j = 0; j < n; j++) {
      cin >> a[j];
    }
    for (int j = 0; j < q; j++) {
      int l, r;
      cin >> l >> r;
      cout << solve(l, r) << endl;
    }
  }
}
