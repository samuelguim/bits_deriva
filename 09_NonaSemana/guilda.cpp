#include <iostream>
#include <vector>

using namespace std;

class UnionFind
{
private:
    vector<int> pai, rank, soma_pontos;

public:
    UnionFind(int tamanho, const vector<int> &pontos)
    {
        pai.resize(tamanho);
        rank.assign(tamanho, 1);
        soma_pontos = pontos;
        for (int i = 0; i < tamanho; i++)
        {
            pai[i] = i;
        }
    }

    int find(int p)
    {
        if (pai[p] != p)
        {
            pai[p] = find(pai[p]);
        }
        return pai[p];
    }

    void union_sets(int p, int q)
    {
        int raizP = find(p);
        int raizQ = find(q);

        if (raizP != raizQ)
        {
            if (rank[raizP] > rank[raizQ])
            {
                pai[raizQ] = raizP;
                soma_pontos[raizP] += soma_pontos[raizQ];
            }
            else if (rank[raizP] < rank[raizQ])
            {
                pai[raizP] = raizQ;
                soma_pontos[raizQ] += soma_pontos[raizP];
            }
            else
            {
                pai[raizQ] = raizP;
                soma_pontos[raizP] += soma_pontos[raizQ];
                rank[raizP]++;
            }
        }
    }

    int get_soma_pontos(int p)
    {
        return soma_pontos[find(p)];
    }
};

int main()
{
    while (true)
    {
        int N, M;
        cin >> N >> M;
        if (N == 0 && M == 0)
            break;

        vector<int> pontos(N);
        for (int i = 0; i < N; i++)
        {
            cin >> pontos[i];
        }

        UnionFind uf(N, pontos);
        int vitorias = 0;

        for (int i = 0; i < M; i++)
        {
            int Q, A, B;
            cin >> Q >> A >> B;
            A--;
            B--;

            if (Q == 1)
            {
                uf.union_sets(A, B);
            }
            else if (Q == 2)
            {
                if (uf.get_soma_pontos(A) > uf.get_soma_pontos(B) && uf.find(0) == uf.find(A))
                {
                    vitorias++;
                }
                else if (uf.get_soma_pontos(B) > uf.get_soma_pontos(A) && uf.find(0) == uf.find(B))
                {
                    vitorias++;
                }
            }
        }

        cout << vitorias << endl;
    }
    return 0;
}