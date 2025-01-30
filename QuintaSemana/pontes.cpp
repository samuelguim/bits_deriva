#include <iostream>
#include <list>
#include <cstdio>

using namespace std;

bool confereSomaSubset(int elementos[], int n, int soma){
    if (soma == 0){
        return true;}
    if (n < 0) {
        return false;}

    bool soma_subset[n][soma+1];

    for(int i = 0; i < n; i++){
        soma_subset[0][i] = true;
    }

    for(int i = 1; i <= soma; i++){
        for (int j = 0; j < n; j++){
            soma_subset[i][j] = (soma_subset[i-1][j] || soma_subset[i-1][j-elementos[j]]);
        }
    }
    
    return soma_subset[n-1][soma];
}

int main(){
    list<char> respostas;
    int r, k;
    while(cin>>r>>k){
        list<int> regioes[r];
        int pontes_por_regiao[r];
        for(int i = 0; i < r; i++){
            regioes[i] = {};
        }
        for (int i = 0; i < k; i++){
            int inicio, destino;
            cin >> inicio >> destino;
            //cuidado com erros na lista
            regioes[inicio-1].push_back(destino-1);
            regioes[destino-1].push_back(inicio-1);
        }
        for (int i = 0; i < r; i++){
            pontes_por_regiao[i] = regioes[i].size();
        }

        if (confereSomaSubset(pontes_por_regiao, r, k) == true){
            respostas.push_back('S');
        }
        else {
            respostas.push_back('N');
        }
    }
    for (auto i : respostas){
        cout << i << "\n";
    }
    return 0;
}