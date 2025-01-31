#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int mochila_cheia(int cap, const vector<pair<int, int>>& itens) {
    vector<int> dp(cap + 1, 0);
    vector<bool> valido(cap + 1, false);
    valido[0] = true;  

    for (int i = 0; i <= cap; i++) {
        for (const auto& item : itens) {
            int qtd = item.first;
            int valor = item.second;
            if (i - qtd >= 0 && valido[i - qtd]) {
                dp[i] = max(dp[i], dp[i - qtd] + valor);
                valido[i] = true;
            }
        }
    }

    return dp[cap];
}

int main() {

    vector<int> resultados;
    int n_promocoes, qtd_latas;
    
    while (cin >> n_promocoes >> qtd_latas) {
        vector<pair<int, int>> promocoes(n_promocoes);
        for (int i = 0; i < n_promocoes; i++) {
            cin >> promocoes[i].first >> promocoes[i].second;
        }
        
        int resposta = mochila_cheia(qtd_latas, promocoes);
        resultados.push_back(resposta);
    }

    for (int res : resultados) {
        cout << res << endl;
    }

    return 0;
}
