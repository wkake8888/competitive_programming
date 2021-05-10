#include <iostream>
#include <map>
using namespace std;

int main() {
	int n;
    cin >> n;
    string s[100001];
    map<string, int> Map;
    for (int i = 1; i <= n; i++) {
        cin >> s[i];
        if (Map[s[i]] == 0) {
            Map[s[i]] = 1;
            cout << i << endl;
        }
    }
}