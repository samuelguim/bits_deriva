#include <iostream>
#include <math.h>
#include <iomanip>
#include <vector>

using namespace std;

int main(){
    vector <float> respostas;
    float mA, mB, mC;
    while (cin >> mA >> mB >> mC){
        float s = (mA + mB + mC)/2;
        float area = 1.3333*(sqrt(s*(s-mA)*(s-mB)*(s-mC)));
        //cout << setprecision(3) << area << "\n";
        respostas.push_back(area);
    }
    for(int i = 0; i++; i <= respostas.size()){
        cout << setprecision(3) << respostas[i] << "\n";
    }
    return 0;
}

