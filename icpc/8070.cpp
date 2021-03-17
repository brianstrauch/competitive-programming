#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
  int n, k;
  while (cin >> n >> k) {
    int idx = 0;

    stack<int> history;
    history.push(idx);

    for (int i = 0; i < k; i++) {
      string cmd;
      cin >> cmd;
      if (cmd == "undo") {
        int m;
        cin >> m;
        for (int j = 0; j < m; j++) {
          history.pop();
        }
        idx = history.top();
      } else {
        int p = stoi(cmd);
        idx = (idx + p) % n;
        if (idx < 0) {
          idx += n;
        }
        history.push(idx);
      }
    }

    cout << idx << endl;
  }
}
