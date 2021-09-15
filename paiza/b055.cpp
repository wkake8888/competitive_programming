#include <iostream>
using namespace std;
int main(void){
    int n, x, mi = 100000 * 5000, cost, mx = 0, a_i, b_i, c_i, d_i;
    cin >> n >> x;

    for (int i = 0; i < n; i++) {
        cin >> a_i >> b_i >> c_i >> d_i;
        if (a_i > x) cost = b_i;
        else {
            cost = b_i + ((x - a_i) / c_i + 1) * d_i;
        }
        if (cost > mx) mx = cost;
        if (cost < mi) mi = cost;
    }

    cout << mi << " " << mx << endl;
}