#include <iostream>
#include <vector>
#include <sstream>
#include <limits>
#include <iomanip>

using namespace std;

int main()
{
    string line;
    vector<string> dados;

    while (getline(cin, line))
    {
        stringstream ss(line);
        string token;
        while (ss >> token)
        {
            dados.push_back(token);
        }
    }

    int indice = 0;
    while (true)
    {
        int num_itens = stoi(dados[indice]);
        int num_produtos = stoi(dados[indice + 1]);
        indice += 2;

        if (num_itens == 0 && num_produtos == 0)
        {
            break;
        }

        vector<int> requisitos_itens;
        for (int i = 0; i < num_itens; ++i)
        {
            requisitos_itens.push_back(stoi(dados[indice + i]));
        }
        indice += num_itens;

        vector<pair<int, double>> informacoes_produtos;
        for (int i = 0; i < num_produtos; ++i)
        {
            int item_necessario = stoi(dados[indice]);
            double preco = stod(dados[indice + 1]);
            informacoes_produtos.push_back(make_pair(item_necessario, preco));
            indice += 2;
        }

        vector<double> custo_minimo(num_itens + 1, numeric_limits<double>::infinity());
        custo_minimo[0] = 0.0;

        for (const auto &produto : informacoes_produtos)
        {
            int item_necessario = produto.first;
            double preco = produto.second;
            for (int i = num_itens - 1; i >= 0; --i)
            {
                if (custo_minimo[i] != numeric_limits<double>::infinity() && requisitos_itens[i] == item_necessario)
                {
                    if (custo_minimo[i + 1] > custo_minimo[i] + preco)
                    {
                        custo_minimo[i + 1] = custo_minimo[i] + preco;
                    }
                }
            }
        }

        if (custo_minimo[num_itens] != numeric_limits<double>::infinity())
        {
            cout << fixed << setprecision(2) << custo_minimo[num_itens] << endl;
        }
        else
        {
            cout << "Impossible" << endl;
        }
    }

    return 0;
}