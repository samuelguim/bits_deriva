#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void update(vector<vector<int>>& ft, int max_x, int max_y, int x, int y, int valor) {
    int i = x;
    while (i <= max_x) {
        int j = y;
        while (j <= max_y) {
            ft[i][j] += valor;
            j += j & -j;
        }
        i += i & -i;
    }
}

int query(const vector<vector<int>>& ft, int x, int y) {
    if (x < 0 || y < 0) return 0;
    int s = 0;
    int i = x;
    while (i > 0) {
        int j = y;
        while (j > 0) {
            s += ft[i][j];
            j -= j & -j;
        }
        i -= i & -i;
    }
    return s;
}

int range_soma(const vector<vector<int>>& ft, int x_inicio, int y_inicio, int x_final, int y_final) {
    return query(ft, x_final, y_final)
        - query(ft, x_inicio - 1, y_final)
        - query(ft, x_final, y_inicio - 1)
        + query(ft, x_inicio - 1, y_inicio - 1);
}

int main() {
    vector<int> resultados;
    while (true) {
        int x, y, p;
        cin >> x >> y >> p;
        if (x == 0 && y == 0 && p == 0) break;

        vector<vector<int>> campo(x + 1, vector<int>(y + 1, 0));

        int q;
        cin >> q;
        for (int i = 0; i < q; ++i) {
            string msg;
            cin >> msg;

            if (msg == "A") {
                int N, xi, yi;
                cin >> N >> xi >> yi;
                update(campo, x, y, xi + 1, yi + 1, N);
            } else {
                int x1, y1, x2, y2;
                cin >> x1 >> y1 >> x2 >> y2;
                int custo = range_soma(campo, min(x1, x2) + 1, min(y1, y2) + 1, max(x1, x2) + 1, max(y1, y2) + 1);
                resultados.push_back(custo * p);
            }
        }

        resultados.push_back(-1);
    }

    for (int res : resultados) {
        if (res == -1) {
            cout << endl;
        } else {
            cout << res << endl;
        }
    }

    return 0;
}
