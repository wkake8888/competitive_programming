#include <iostream>
using namespace std;

int main() {
    long long n , k;
    cin >> n >> k;

    for (int i = 0; i < k; i++) {
        if (n % 200 == 0) n /= 200;
        else {
            string a = to_string(n);
            a += "200";
            n = stoll(a);
        }
    }
    cout << n << endl;
}