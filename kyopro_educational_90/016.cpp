#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, a, b, c, count, mi = 2147483647, k;
    cin >> n >> a >> b >> c;

    for (int i = 0; i <= 9999; i++) {
        for (int j = 0; j <= 9999 - i; j++) {
            long long l = n - a * i - b * j;
            k = l / c;
            count = i + j + k;
            if (l % c != 0 || l < 0 || count > 9999) continue;
            mi = min(mi, count);
        }
    }

    cout << mi << endl;
}