// 1296 Medianas
// bits à deriva
// Samuel Guimarães Silva
// João Guilherme Alves
// Caio Vinicius da Cruz Coelho

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <iomanip>
#include <vector>

using namespace std;

bool verificaExistencia(double l1, double l2, double l3){
    if (l1 == 0 || l2 == 0 || l3 ==0){
        return false;
    }
    else if (l3 >=(l1 + l2)){
        return false;
    }
    else if (l2 >=(l1 + l3)){
        return false;
    }
    else if (l1 >=(l3 + l2)){
        return false;
    }
    return true;
}

int main(){
    vector <double> respostas;
    double mA, mB, mC;
    while (cin >> mA >> mB >> mC){
        double area;
        if (verificaExistencia(mA, mB, mC)){
            double s = (mA + mB + mC)/2;
            area = 1.33333333333333*(sqrt(s*(s-mA)*(s-mB)*(s-mC)));
        }
        else{
            area = -1.000;
        }
        respostas.push_back(area);
    }
    for(int i = 0; i < respostas.size(); i++){
        printf("%.3f\n", respostas[i]);
    }
    return 0;
}

