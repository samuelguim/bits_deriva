#include <stdio.h>
#include <string.h>
#include <stdbool.h>


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

    for (int i = 0; i < m; i++){
        char nomePorcao[50];
        int quantIngr = 0;
        scanf("%s %i", nomePorcao, &quantIngr);

        char ingredientes_temp[quantIngr*50];
        char ingredientes [quantIngr][50];
        scanf(" %[^\n]s", ingredientes_temp);
        int j = 0;

        //evita bug array corrompido
        char tipicos2[n][50];
        for (int i = 0; i < n; i++){
            strcpy(tipicos2[i], tipicos[i]);
        }


        for (int i = 0; i < quantIngr; i++){
            int k = 0;
            while(ingredientes_temp[j] != ' ' && j < n*50){
                ingredientes[i][k] = ingredientes_temp[j];
                j++;
                k++;
            }
            j++;
        }
        
        // conta quantos ingredientes são típicos
        int contador = 0;
        for(int i = 0; i < quantIngr; i++){
            for (int j = 0; j < n; j++){
                if (strcmp(ingredientes[i], tipicos2[j]) == 0){
                    contador++;
                }
            }
        }

        // conta quantos ingredientes são porções típicas
        char porcoesTipicas[50][m];
        for(int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (strcmp(ingredientes[i], tipicos2[j]) == 0){
                    contador++;
                }
            }
        }
        
        // define se a porção é típica ou comum
        if (contador > quantIngr/2){
            printf("porcao tipica\n");
        }
        else {
            printf("porcao comum\n");
        }
    }
    
    return 0;
}