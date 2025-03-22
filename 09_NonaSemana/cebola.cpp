#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

struct Ponto {
    double x, y;
};

vector<Ponto> graham_scan(vector<Ponto> pontos) {
    if (pontos.size() <= 3) return pontos; // casos triviais
    
    // encontra o ponto com menor coordenada y (e mais à esquerda em caso de empate)
    int idx_minimo = 0;
    for (int i = 1; i < pontos.size(); i++) {
        if (pontos[i].y < pontos[idx_minimo].y || 
            (pontos[i].y == pontos[idx_minimo].y && pontos[i].x < pontos[idx_minimo].x)) {
            idx_minimo = i;
        }
    }
    
    // coloca o ponto inicial na primeira posição
    swap(pontos[0], pontos[idx_minimo]);
    Ponto ponto_inicial = pontos[0];
    
    // ordena os pontos pelo ângulo polar em relação ao ponto_inicial
    sort(pontos.begin() + 1, pontos.end(), [&ponto_inicial](const Ponto& p1, const Ponto& p2) {
        // calcula o produto vetorial para determinar qual ponto tem menor ângulo
        double prod = (p1.x - ponto_inicial.x) * (p2.y - ponto_inicial.y) - 
                      (p1.y - ponto_inicial.y) * (p2.x - ponto_inicial.x);
        
        if (prod == 0) {
            // se colineares, escolhe o mais próximo primeiro
            double dist1 = pow(p1.x - ponto_inicial.x, 2) + pow(p1.y - ponto_inicial.y, 2);
            double dist2 = pow(p2.x - ponto_inicial.x, 2) + pow(p2.y - ponto_inicial.y, 2);
            return dist1 < dist2;
        }
        
        return prod > 0; // ordenação anti-horária
    });
    
    // função para determinar se temos uma curva à esquerda, direita ou colinear
    auto produto_vetorial = [](const Ponto& p1, const Ponto& p2, const Ponto& p3) -> double {
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);
    };
    
    // inicializa a pilha com os primeiros pontos
    vector<Ponto> pilha;
    pilha.push_back(pontos[0]);
    pilha.push_back(pontos[1]);
    
    // para cada ponto ordenado pelo ângulo
    for (int i = 2; i < pontos.size(); i++) {
        // enquanto temos pelo menos 2 pontos na pilha e o último movimento não forma uma curva à esquerda
        while (pilha.size() >= 2 && produto_vetorial(pilha[pilha.size() - 2], pilha[pilha.size() - 1], pontos[i]) <= 0) {
            // remove o último ponto da pilha
            pilha.pop_back();
        }
        
        // adiciona o ponto atual à pilha
        pilha.push_back(pontos[i]);
    }
    
    // a pilha final contém os pontos do fecho convexo
    return pilha;
}

int main(){
    int N;
    cin >> N;
    while (N != 0){
        for (int i = 0; i < N; i++){
            int x, y;
            cin >> x >> y;
            
        }
    }
    return 0;
}