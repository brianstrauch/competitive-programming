#include <iostream>
#include <string>
using namespace std;

int m, n;
char arr[100][100];
bool v[100][100];

void dfs(int i, int j) {
  if (i < 0 || i >= m || j < 0 || j >= n) {
    return;
  }
  if (arr[i][j] == '.' || v[i][j]) {
    return;
  }
  v[i][j] = true;

  dfs(i - 1, j - 1);
  dfs(i - 1, j);
  dfs(i - 1, j + 1);
  dfs(i, j - 1);
  dfs(i, j + 1);
  dfs(i + 1, j - 1);
  dfs(i + 1, j);
  dfs(i + 1, j + 1);
}

int solve() {
  int count = 0;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (arr[i][j] == '#' && !v[i][j]) {
        dfs(i, j);
        count++;
      }
    }
  }
  return count;
}

int main() {
  while (cin >> m >> n) {
    for (int i = 0; i < m; i++) {
      string row;
      cin >> row;
      for (int j = 0; j < n; j++) {
        arr[i][j] = row[j];
        v[i][j] = false;
      }
    }

    cout << solve() << endl;
  }
}
