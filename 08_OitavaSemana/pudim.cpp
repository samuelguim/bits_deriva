#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lcs(const string &a, const string &b) {
    int n = a.size(), m = b.size();
    vector<int> dp(m + 1, 0);

    for (int i = 1; i <= n; i++) {
        int prev = dp[0];
        for (int j = 1; j <= m; j++) {
            int temp = dp[j]; 
            if (a[i - 1] == b[j - 1]) {
                dp[j] = 1 + prev;
            } else {
                dp[j] = max(dp[j - 1], dp[j]);
            }
            prev = temp;
        }
    }

    return dp[m];
}

int main() {
    string p1, p2;
    cin >> p1 >> p2;
    cout << lcs(p1, p2) << endl;
    return 0;
}