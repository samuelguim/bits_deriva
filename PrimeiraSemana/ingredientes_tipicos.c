#include <stdio.h>
#include <string.h>
#include <stdbool.h>


bool confereTipico (int i, int n, int m, int quantIngr, char ingredientes[quantIngr][m][50], char porcoesTipicas[50][m], char tipicos2[n][50]){
    int contador = 0;
    for(int k = 0; k < quantIngr; k++){
        for (int j = 0; j < n; j++){
            if (strcmp(ingredientes[i][k], tipicos2[j]) == 0){
                contador++;
            }
        }
    }
    
    // conta quantos ingredientes são porções típicas
    for(int k = 0; k < quantIngr; k++){
        for (int j = 0; j < m; j++){
            if (strcmp(ingredientes[i][k], porcoesTipicas[j]) == 0){
                contador++;
            }
        }
    }
    if(quantIngr != 0){
        if (contador > quantIngr/2){
        return true;
    }
    }
    else {
        return false;
    }
}


int main(){

    //lê os ingredientes típicos
    int n, m;
    scanf("%i", &n);
    char tipicos_temp[n*50];
    scanf(" %[^\n]s", tipicos_temp);
    
    char tipicos[n][50];
    int j = 0;
    for (int i = 0; i < n; i++){
        int k = 0;
        while(tipicos_temp[j] != ' ' && j < n*50){
            tipicos[i][k] = tipicos_temp[j];
            j++;
            k++;
        }
        j++;
    }

    scanf("%i", &m);
    char tiposDePorcao[m][13];
    char porcoesTipicas[50][m];

    for (int i = 0; i < m; i++){
        char nomePorcao[50];
        int quantIngr = 0;
        scanf("%s %i", nomePorcao, &quantIngr);

        char ingredientes_temp[m][quantIngr*50];
        char ingredientes[m][quantIngr][50];
        scanf(" %[^\n]s", ingredientes_temp[i]);
        int j = 0;

        //evita bug array corrompido
        char tipicos2[n][50];
        for (int i = 0; i < n; i++){
            strcpy(tipicos2[i], tipicos[i]);
        }


        for (int l = 0; l < quantIngr; l++){
            int k = 0;
            while(ingredientes_temp[i][j] != ' ' && j < n*50){
                ingredientes[i][l][k] = ingredientes_temp[i][j];
                j++;
                k++;
            }
            j++;
        }
        
        if (confereTipico(i, n, m, quantIngr, ingredientes, porcoesTipicas, tipicos2)){
            strcpy(tiposDePorcao[i],"porcao tipica");
            //printf("porcao tipica\n");
        }
        else {
            strcpy(tiposDePorcao[i],"porcao comum");
            //printf("porcao comum\n");
        }

        if (i == m-1){
            for (int p = 0; p < m; p++){
                printf("%s\n", tiposDePorcao[p]);
            }
        }
    }
    
    return 0;
}