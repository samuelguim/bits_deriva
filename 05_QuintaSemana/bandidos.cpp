#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

vector<vector<int>> gerar_grafo_invertido(const vector<int>& grafo) {
    int n = grafo.size() - 1;
    vector<vector<int>> grafo_inv(n + 1);
    for (int no = 2; no <= n; no++) {
        int superior = grafo[no];
        if (superior != 0)
            grafo_inv[superior].push_back(no);
    }
    return grafo_inv;
}

vector<int> maior_altura(int raiz, const vector<vector<int>>& grafo_inv) {
    int n = grafo_inv.size() - 1;
    vector<int> altura(n + 1, 0);
    queue<pair<int, int>> q;
    q.push({raiz, 1});
    while (!q.empty()){
        auto [atual, h] = q.front();
        q.pop();
        altura[atual] = h;
        for (int child : grafo_inv[atual]) {
            q.push({child, h + 1});
        }
    }
    vector<int> nodes;
    for (int i = 1; i <= n; i++){
        nodes.push_back(i);
    }
    sort(nodes.begin(), nodes.end(), [&altura](int a, int b) {
        return altura[a] > altura[b];
    });
    return nodes;
}

vector<int> pegar_folhas(const vector<int>& grafo) {
    int n = grafo.size() - 1;
    unordered_set<int> pais;
    for (int i = 1; i <= n; i++){
        pais.insert(grafo[i]);
    }
    vector<int> folhas;
    for (int i = 1; i <= n; i++){
        if (pais.find(i) == pais.end())
            folhas.push_back(i);
    }
    return folhas;
}

int pegar_altura(int no, const vector<int>& grafo, vector<bool>& visitados) {
    int c = 0;
    while (no != 1) {
        if (!visitados[no]) {
            c++;
            visitados[no] = true;
        }
        no = grafo[no];
        if (no == 1 && !visitados[1]) {
            c++;
            visitados[1] = true;
        }
    }
    return c;
}

int prender(const vector<int>& grafo, int nSelecionados) {
    vector<int> folhas = pegar_folhas(grafo);
    unordered_set<int> folhasSet(folhas.begin(), folhas.end());
    vector<bool> visitados(grafo.size(), false);
    
    vector<vector<int>> grafo_inv = gerar_grafo_invertido(grafo);
    vector<int> sorted_nodes = maior_altura(1, grafo_inv);
    
    vector<int> alturas;
    for (int node : sorted_nodes) {
        if (folhasSet.count(node))
            alturas.push_back(pegar_altura(node, grafo, visitados));
    }
    
    sort(alturas.begin(), alturas.end(), greater<int>());
    int resultado = 0;
    for (int i = 0; i < nSelecionados && i < (int)alturas.size(); i++){
        resultado += alturas[i];
    }
    return resultado;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int qtd_membros, previsoes;
    cin >> qtd_membros >> previsoes;
    
    vector<int> grafo(qtd_membros + 1);
    grafo[1] = 1;
    for (int i = 2; i <= qtd_membros; i++){
        cin >> grafo[i];
    }
    
    cout << prender(grafo, previsoes) << "\n";
    return 0;
}