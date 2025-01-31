#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int bfs_teste(map<int, vector<int>>& grafo, int no_inicial, vector<char>& sons, vector<int>& visitados) {
    int contador = 0;
    queue<int> q;
    q.push(no_inicial);
    
    while (!q.empty()) {
        int no = q.front();
        q.pop();
        
        if (visitados[no] == 0) {
            visitados[no] = 1;
            if (sons[no] == 'B') {
                contador++;
            }
            for (int vizinho : grafo[no]) {
                if (visitados[vizinho] == 0) {
                    q.push(vizinho);
                }
            }
        }
    }
    return contador;
}

int main() {
    vector<char> resultados;
    
    while (true) {
        int qtd_torres, m;
        if (!(cin >> qtd_torres >> m)) break;
        
        vector<char> sons_iniciais(qtd_torres);
        for (int i = 0; i < qtd_torres; i++) {
            cin >> sons_iniciais[i];
        }
        
        map<int, vector<int>> conexoes;
        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            conexoes[a - 1].push_back(b - 1);
            conexoes[b - 1].push_back(a - 1);
        }
        
        vector<int> lista_visitados(qtd_torres, 0);
        bool possivel = true;
        
        for (int i = 0; i < qtd_torres; i++) {
            if (lista_visitados[i] == 0) {
                int contador = bfs_teste(conexoes, i, sons_iniciais, lista_visitados);
                if (contador % 2 != 0) {
                    possivel = false;
                    break;
                }
            }
        }
        
        resultados.push_back(possivel ? 'Y' : 'N');
    }
    
    for (char res : resultados) {
        cout << res << '\n';
    }
    
    return 0;
}