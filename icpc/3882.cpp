#include <iostream>
#include <vector>
using namespace std;

int solve(int n, int k, int m) {
  vector<int> stones(n);
  for (int i = 0; i < n; i++) {
    stones[i] = i + 1;
  }

  int idx = m - 1;
  while (stones.size() > 1) {
    stones.erase(stones.begin() + idx);
    idx = (idx + k - 1) % stones.size();
  }
  return stones[0];
}

int main() {
  int n, k, m;
  while (true) {
    cin >> n >> k >> m;
    if (n == 0 && k == 0 && m == 0) {
      break;
    }
    cout << solve(n, k, m) << endl;
  }
}
