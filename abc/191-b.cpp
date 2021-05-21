#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x, y;
    cin >> n >> x;

    for (int i = 0; i < n; i++) {
        cin >> y;
        if (y == x) continue;
        else {
            if (i == n - 1) cout << y;
            else cout << y << " ";
        }
    }
}