#include <iostream>
using namespace std;

int main() {
	long long n, k, diff = 0;
    cin >> n >> k;
    int A[1001], B[1001];

    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];

    for (int i = 0; i < n; i++) {
        diff += abs(A[i] - B[i]);
    }

    if (k > diff && k - diff % 2 == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
}