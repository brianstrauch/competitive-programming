#include <iostream>
using namespace std;

int solve(int a[], int n, int k) {
  int count = 0;
  int i = 0;
  while (i < n - k + 1) {
    int min = a[i];
    int idx = i;
    for (int j = i + 1; j < i + k; j++) {
      if (a[j] < min) {
        min = a[j];
        idx = j;
      }
    }
    count += min;
    for (int j = idx + 1; j < i + k; j++) {
      a[j] -= min;
    }
    i = idx + 1;
  }
  return count;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n, k;
    cin >> n >> k;
    int a[n];
    for (int j = 0; j < n; j++) {
      cin >> a[j];
    }
    cout << solve(a, n, k) << endl;
  }
}
