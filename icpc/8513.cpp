#include <algorithm>
#include <iostream>
using namespace std;

int solve(int a[], int b[], int n, int k) {
  sort(a, a + n);
  sort(b, b + n);

  int count = 0;
  int j = n - 1;
  for (int i = 0; i < n; i++) {
    if (a[i] + b[j] >= k) {
      count++;
      j--;
    }
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
    int b[n];
    for (int j = 0; j < n; j++) {
      cin >> b[j];
    }

    cout << solve(a, b, n, k) << endl;
  }
}
