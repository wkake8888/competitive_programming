#include <iostream>
using namespace std;

long long w, d, h, z, a;
long long eua(long long x, long long y) {
    while (x % y != 0) {
        z = x % y;
        x = y;
        y = z;
    }
    return y;
}
int main() {
	cin >> w >> d >> h;
    a = eua(eua(w, d), h);

    cout << (w / a - 1) + (h / a - 1) + (d / a - 1) << endl;
}

