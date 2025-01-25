#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>

using namespace std;

int posicao_diferenca_string(string a, string b){
    //obtem a quantidade de caracteres da menor string
    int tamanho_a = a.size();
    int tamanho_b = b.size();

    int n = 0;
    if (tamanho_a > tamanho_b){
        n = tamanho_b;
    }
    else {
        n = tamanho_a;
    }

    //procura a diferença
    int diferenca = 0;
    for(int i = 0; i < n; i++){
        if (a[i] != b[i]){
            diferenca = i+1;
            break;
        }
    }

    if (diferenca == 0){
        if (tamanho_a > tamanho_b){
            diferenca = tamanho_b+1;
        }
        else if (tamanho_a < tamanho_b){
            diferenca = tamanho_a+1;
        }
    }

    return diferenca;
}

void troca_simples(string palavras[], int a, int b){
    string temp = palavras[a];
    palavras[a] = palavras[b];
    palavras[b] = temp;
}

void trocar_palavras(string palavras[], int a, int b){
    for (int i = a; i < b; i++){
        int prox = i + 1;
        troca_simples(palavras, i, prox);
    }
}

int main(){
    int n, k;
    int instancia = 0;
    string str_instancia;
    vector<string> resultadofinal;
    
    while (true) {
        cin >> n >> k;
        if (n == 0 && k == 0){
            break;
        }

        string alunos[n];

        for(int i = 0; i < n; i++){
            cin >> alunos[i];
        }

        str_instancia = "Instancia " + to_string(instancia + 1);
        resultadofinal.push_back(str_instancia);
        resultadofinal[instancia] = resultadofinal[instancia] + "\n";

        //busca a maior diferença na ordem lexicográfica
        int menor_posicao = 20;
        int maior_diferenca = 0;
        int posicao_a_trocar = 0;
        int trocas_realizadas = 0;

        for(int j = 0; j < n; j++){
            for(int i = 1; i <= k; i++){
                int proximo = j + i;
                if(sizeof(alunos) < proximo){
                    if (posicao_diferenca_string(alunos[j], alunos[proximo]) <  menor_posicao && posicao_diferenca_string(alunos[j], alunos[proximo]) !=0){
                        if (alunos[j].compare(alunos[proximo]) > maior_diferenca){
                            menor_posicao = posicao_diferenca_string(alunos[j], alunos[proximo]);
                            maior_diferenca = alunos[j].compare(alunos[proximo]);
                            posicao_a_trocar = i;
                        }
                    }
                }
            }
            int prox = posicao_a_trocar + 1;
            trocar_palavras(alunos, posicao_a_trocar, prox);
        }

        //imprime o resultado
        for(int i = 0; i < n; i++){
            resultadofinal[instancia] = resultadofinal[instancia] + alunos[i] + " ";
        }
    
    resultadofinal[instancia] = resultadofinal[instancia] + "\n\n";
    instancia++;
    }

    for (int i = 0; i < resultadofinal.size(); i++){
        cout << resultadofinal[i];
    };
    return 0;
}