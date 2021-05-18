#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int n, ans = 0;
    cin >> n;
    vector<long long int> A(n), B(n);
    for (long long int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (long long int i = 0; i < n; i++) {
        cin >> B[i];
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    for (long long int i = 0; i < n; i++) {
        ans += abs(A[i] - B[i]);
    }

    cout << ans << endl;
}