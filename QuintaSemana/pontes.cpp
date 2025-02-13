// 1203 Pontes de São Petersburgo
// bits à deriva
// Samuel Guimarães Silva
// João Guilherme Alves
// Caio Vinicius da Cruz Coelho

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

bool confereSomaSubset(const int elementos[], int n, int soma) {
    if (soma == 0) return true;
    if (n == 0) return false;

    int total = 0;
    for (int i = 0; i < n; ++i) {
        total += elementos[i];
    }
    if (soma > total) return false;

    vector<bool> dp(soma + 1, false);
    dp[0] = true;

    for (int i = 0; i < n; ++i) {
        for (int j = soma; j >= elementos[i]; --j) {
            if (dp[j - elementos[i]]) {
                dp[j] = true;
                if (j == soma) break;
            }
        }
    }

    return dp[soma];
}

int main() {
    vector<char> respostas;
    int r, k;
    while (cin >> r >> k) {
        vector<int> pontes_por_regiao(r, 0);
        for (int i = 0; i < k; ++i) {
            int inicio, destino;
            cin >> inicio >> destino;
            pontes_por_regiao[inicio - 1]++;
            pontes_por_regiao[destino - 1]++;
        }

        if (confereSomaSubset(pontes_por_regiao.data(), r, k)) {
            respostas.push_back('S');
        } else {
            respostas.push_back('N');
        }
    }

    for (char res : respostas) {
        cout << res << "\n";
    }

    return 0;
}