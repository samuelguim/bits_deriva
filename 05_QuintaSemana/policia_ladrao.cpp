#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Pos
{
    int x, y;
};

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

bool isValid(int x, int y, vector<vector<int>> &matriz, vector<vector<bool>> &visitado)
{
    return x >= 0 && x < 5 && y >= 0 && y < 5 && matriz[x][y] == 0 && !visitado[x][y];
}

bool bfs(vector<vector<int>> &matriz)
{
    queue<Pos> fila;
    vector<vector<bool>> visitado(5, vector<bool>(5, false));

    fila.push({0, 0});
    visitado[0][0] = true;

    while (!fila.empty())
    {
        Pos atual = fila.front();
        fila.pop();

        if (atual.x == 4 && atual.y == 4)
        {
            return true;
        }

        for (int i = 0; i < 4; i++)
        {
            int nx = atual.x + dx[i];
            int ny = atual.y + dy[i];

            if (isValid(nx, ny, matriz, visitado))
            {
                visitado[nx][ny] = true;
                fila.push({nx, ny});
            }
        }
    }

    return false;
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        vector<vector<int>> matriz(5, vector<int>(5));

        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                cin >> matriz[i][j];
            }
        }

        if (bfs(matriz))
        {
            cout << "COPS" << endl;
        }
        else
        {
            cout << "ROBBERS" << endl;
        }
    }

    return 0;
}
