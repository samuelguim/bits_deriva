// O código em c++ não funciona para números arbitrariamente grandes

// 1839 A Câmara Secreta
// bits à deriva
// Samuel Guimarães Silva
// João Guilherme Alves
// Caio Vinicius da Cruz Coelho

#include <iostream>
#include <vector>

using namespace std;

long long fatorial_ate(int numero, int parada){
    long long fatorial = numero;
    if (numero == 0 || numero == 1){
        return 1;
    }
    for(int i = 1; i < parada; i++){
        fatorial = fatorial * (numero - i);
    }
    return fatorial;
}

int main(){    
    vector <long long> respostas;
    int N, M;
    cin >> N >> M;

    string grid[N];
    for (int i = 0; i < N; i++){
        cin >> grid[i];
    }

    int xA, yA, xB, yB;
    while (cin >> xA >> yA >> xB >> yB){
        int comprimento = (xB - xA + 1);
        int largura = (yB - yA + 1);
        int tamanhoRegiao = comprimento * largura;
        int paredes = 0;
        for(int i = yA-1; i < yB; i++){
            for(int j = xA-1; j < xB; j++){
                if (grid[j][i] == '#'){
                    paredes++;
                }
            }
        }

        long long combinacoes;
        if(paredes == 0){
            combinacoes = 0;
        }
        else {
            combinacoes = fatorial_ate(tamanhoRegiao, paredes) / fatorial_ate(paredes, paredes);
            combinacoes = (combinacoes -1) % 1000000007;
        }

        respostas.push_back(combinacoes);
    }

    for (int i = 0; i < respostas.size(); i++){
        cout << respostas[i] << "\n";
    }

    return 0;
}