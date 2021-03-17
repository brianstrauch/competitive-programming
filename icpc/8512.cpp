#include <algorithm>
#include <iostream>
using namespace std;

int n, q, k;
int a[10000];

int solve(int l, int r) {
  l--;
  r--;

  int m = 0;
  for (int i = l; i <= r; i++) {
    for (int j = i + 1; j <= r; j++) {
      m = max(m, a[i] ^ a[j]);
    }
  }
  return m | k;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> n >> q >> k;
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
