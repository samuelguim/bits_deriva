#include <stdio.h>

int main(){
    int n, m, a, b;
    
    while (1){
        scanf("%i %i", &n, &m);
        if (n == 0 && m == 0){
            break;
        }
        
        char linha[n][m];
        for (int i = 0; i < n; i++){
            scanf("%s", linha[i]);
        }
        scanf("%i %i", &a, &b);

        int multA = a/n;
        int multB = b/m;

        for(int j = 0; j < n; j++){
            for (int ja = 0; ja < multA; ja++){
                for (int k = 0; k < m; k++){
                    for (int kb = 0; kb < multB; kb++){
                        printf("%c", linha[j][k]);
                    }
                }
                printf("\n");
            }
        }
        printf("\n");
    }
    return 0;
}