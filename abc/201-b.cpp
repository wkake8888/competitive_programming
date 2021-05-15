#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, sec_m, m_ind, sec_ind;
    cin >> n;
    vector<string> name(n);
    vector<int> height(n);

    for (int i = 0; i < n; i++) {
        cin >> name[i] >> height[i];
    }

    if (height[0] > height[1]) {
        m = height[0];
        sec_m = height[1];
        m_ind = 0;
        sec_ind = 1;
    }
    else {
        m = height[1];
        sec_m = height[0];
        m_ind = 1;
        sec_ind = 0;
    }
    for (int i = 2; i < n; i++) {
        if (height[i] > m) {
            sec_m = m;
            m = height[i];
            sec_ind = m_ind;
            m_ind = i;
        }
        else if (height[i] > sec_m) {
            sec_m = height[i];
            sec_ind = i;
        }
    }

    cout << name[sec_ind] << endl;
    
    
}