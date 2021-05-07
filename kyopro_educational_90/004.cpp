#include <bits/stdc++.h>
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    vector<vector<int>> vec(h, vector<int>(w));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cin >> vec[i][j];
        }
    }
    vector<int> sum_row(h);
    vector<int> sum_column(w);

    for (int i = 0; i < w; i++) {
        for (int j = 0; j < h; j++) {
            sum_column[i] += vec[j][i];
        }
    }

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            sum_row[i] += vec[i][j];
        }
    }

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            vec[i][j] = sum_row[i] + sum_column[j] - vec[i][j];
        }
    }

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (j == w - 1) cout << vec[i][j] << endl;
            else cout << vec[i][j] << " ";
        }
    }
}