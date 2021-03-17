#include <algorithm>
#include <iostream>
using namespace std;

int n, m;
int c[100], h[100];
int dp[100][100];

int solve() {
  for (int j = 0; j < n; j++) {
    dp[n - 1][j] = min(c[n - 1], h[j]);
  }

  for (int i = n - 2; i >= 0; i--) {
    for (int j = 0; j <= i; j++) {
      int a = min(c[i], h[j]);
      int b = dp[i + 1][j + 1];
      if (i + 2 < n) {
        b = max(b, dp[i + 2][j]);
      }
      if (i + 3 < n) {
        b = max(b, dp[i + 3][0]);
      }

      dp[i][j] = a + b;
    }
  }

  return max(dp[0][0], max(dp[1][0], dp[2][0]));
}

int main() {
  while (cin >> n >> m) {
    for (int i = 0; i < n; i++) {
      cin >> c[i];
      h[i] = m;
      m = 2 * m / 3;
    }
    cout << solve() << endl;
  }
}
