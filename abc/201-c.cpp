#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int count = 0;
    bool flag;
    for (int i = 0; i < 10000; i++) {
        flag = true;
        vector<int> m(10);
        int x = i;
        for (int j = 0; j < 4; j++) {
            m[x%10] = 1;
            x /= 10;
        }
        for (int k = 0; k < 10; k++) {
            if (s[k] == 'o' && m[k] != 1) flag = false;
            if (s[k] == 'x' && m[k] != 0) flag = false;
        }
        if (flag) count++;
    }

    cout << count << endl;
}