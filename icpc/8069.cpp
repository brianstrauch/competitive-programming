#include <iostream>
#include <string>
using namespace std;

int rotation_val(string s) {
  int val = 0;
  for (int i = 0; i < s.length(); i++) {
    val += s[i] - 'A';
  }
  return val;
}

string rotate(string s) {
  int r = rotation_val(s);
  for (int i = 0; i < s.length(); i++) {
    s[i] = (s[i] - 'A' + r) % 26 + 'A';
  }
  return s;
}

string merge(string a, string b) {
  for (int i = 0; i < a.length(); i++) {
    a[i] = (a[i] - 'A' + b[i] - 'A') % 26 + 'A';
  }
  return a;
}

string dec(string c) {
  int m = c.length() / 2;
  string a = c.substr(0, m);
  string b = c.substr(m, m);

  a = rotate(a);
  b = rotate(b);

  return merge(a, b);
}

int main() {
  string c;
  while (cin >> c) {
    cout << dec(c) << endl;
  }
}
