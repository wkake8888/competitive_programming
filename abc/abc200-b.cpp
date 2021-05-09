#include <iostream>
using namespace std;

string divide_str(string s) {
    string ans = "";
    string left = "";
    if (s == "0") return 0;
    else {
        s.erase(-2, -1);
        for (long unsigned int i = 0; i < s.size(); i++) {
            char a = s[i];
            int ia = a - '0';
            ans += to_string(stoi(left + s[i]) / 2);
            left = "";
            if (ia % 2 != 0) left += "1";
        }
    }
    return ans;
}

int main() {
	string n;
    int k;
    cin >> n >> k;

    for (int i = 0; i < k; i++) {
        char a = n[-3];
        int ia = a - '0';
        if (n[-1] == '0' && n[-2] == '0' && ia % 2 == 0) n = divide_str(n);
        else n = to_string(n) + "200";
    }
    cout << n << endl;
}

