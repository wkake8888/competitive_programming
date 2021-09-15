#include <bits/stdc++.h>
using namespace std;

int main() {
    // 配列aにn個の自然数が入っている。
    // minは最小値を表す変数、min_secは配列の中で2番目に小さい値を表す変数
    int min, min_sec;

    // 配列の長さが２未満のときは、エラーを出す
    if (n < 2){
        printf("Invalid Input");
        return;
    }

    // まずminとmin_secを初期化
    if (a[0] > a[1]) {
        min = a[1];
        min_sec = a[0];
    } else {
        min = a[0];
        min_sec = a[1];
    }

    // 配列で2番目に小さい値を探す
    // 初期化の段階で0番目と1番目のインデックスを使っているので、2番目のインデックスから始める
    for (int i = 2; i < n; i++) {
        // もし今の最小値より小さい値があれば、それを最小値にし、今までの最小値を2番目に小さい値に変更する。
        if (a[i] < min) {
            min_sec = min;
            min = a[i];
        } // もし今の最小値以上かつ2番目に小さい値より小さい場合、2番目に小さい値を更新する。
        else if (a[i] < min_sec) {
            min_sec = a[i];
        }
    }

    printf("%d", min_sec);
}