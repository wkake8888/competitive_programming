#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main() {
    long long a, b, c;
    cin >> a >> b >> c;
    long long d = 1;

    for (int i = 1; i <= b; i++) {
        d *= c;
    }
    if (a < d) {
        cout << "Yes" << endl;
    }
    else cout << "No" << endl;
}