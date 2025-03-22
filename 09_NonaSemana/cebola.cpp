#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <unordered_set>

using namespace std;

struct Ponto {
    double x, y;
};

vector<Ponto> graham_scan(vector<Ponto> pontos) {
    if (pontos.size() <= 3) return pontos;
    
    int idx_minimo = 0;
    for (int i = 1; i < pontos.size(); i++) {
        if (pontos[i].y < pontos[idx_minimo].y || 
            (pontos[i].y == pontos[idx_minimo].y && pontos[i].x < pontos[idx_minimo].x)) {
            idx_minimo = i;
        }
    }
    
    swap(pontos[0], pontos[idx_minimo]);
    Ponto ponto_inicial = pontos[0];
    
    sort(pontos.begin() + 1, pontos.end(), [&ponto_inicial](const Ponto& p1, const Ponto& p2) {
        double prod = (p1.x - ponto_inicial.x) * (p2.y - ponto_inicial.y) - 
                      (p1.y - ponto_inicial.y) * (p2.x - ponto_inicial.x);
        
        if (prod == 0) {
            double dist1 = pow(p1.x - ponto_inicial.x, 2) + pow(p1.y - ponto_inicial.y, 2);
            double dist2 = pow(p2.x - ponto_inicial.x, 2) + pow(p2.y - ponto_inicial.y, 2);
            return dist1 < dist2;
        }
        
        return prod > 0;
    });
    
    auto produto_vetorial = [](const Ponto& p1, const Ponto& p2, const Ponto& p3) -> double {
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);
    };
    
    vector<Ponto> pilha;
    pilha.push_back(pontos[0]);
    pilha.push_back(pontos[1]);
    
    for (int i = 2; i < pontos.size(); i++) {
        while (pilha.size() >= 2 && produto_vetorial(pilha[pilha.size() - 2], pilha[pilha.size() - 1], pontos[i]) <= 0) {
            pilha.pop_back();
        }
        
        pilha.push_back(pontos[i]);
    }
    
    return pilha;
}

void remover_pontos(vector<Ponto>& pontos_originais, vector<Ponto>& pontos_a_remover) {
    for (int i = 0; i < pontos_a_remover.size(); i++){
        for (int j = 0; j < pontos_originais.size(); j++){
            if (pontos_a_remover[i].x == pontos_originais[j].x && pontos_a_remover[i].y == pontos_originais[j].y){
                pontos_originais.erase(pontos_originais.begin()+i);
            }
        }
    }
}


int main(){
    int N;
    cin >> N;
    while (N != 0){
        vector <Ponto> pontos;

        Ponto pt;
        for (int i = 0; i < N; i++){
            int x, y;
            cin >> x >> y;
            pt.x = x;
            pt.y = y;
            pontos.push_back(pt);
        }

        int quantidade_camadas = 0;
        vector <Ponto> camada;
        while (pontos.size() > 0){
            camada.clear();
            camada = graham_scan(pontos);
            remover_pontos(pontos, camada);
            quantidade_camadas = quantidade_camadas + 1;
        }
        if (quantidade_camadas % 2 == 0){
            cout << "Take this onion to the lab!!\n";
        }
        else{
            cout << "Do not take this onion to the lab!\n";
        }

        
        cin >> N;
    }
    return 0;
}