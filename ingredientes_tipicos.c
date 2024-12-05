#include <stdio.h>
#include <string.h>


/*
void stringParaArray(char **array, int tamanho){
    int j = 0;
    for (int i = 0; i < tamanho; i++){
        int k = 0;
        while(*array[j] != ' '){
            array[i][k] = *array[j];
            j++;
            k++;
        }
        j++;
    }
}
*/

int main(){

    //lê os ingredientes típicos
    int n, m;
    scanf("%i", &n);
    char tipicos_temp[n*50];
    scanf(" %[^\n]s", tipicos_temp);
    char tipicos[n][50];

    //separa os ingredientes em um array
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
    char nomePorcao[50];
    int quantIngr = 0;

    for (int i = 0; i < m; i++){
        scanf("%s %i", nomePorcao, &quantIngr);
        char ingredientes_temp[quantIngr*50];
        char ingredientes [quantIngr][50];
        scanf(" %[^\n]s", ingredientes_temp);
        int j = 0;
        for (int i = 0; i < quantIngr; i++){
            int k = 0;
            while(ingredientes_temp[j] != ' ' && j < n*50){
                ingredientes[i][k] = ingredientes_temp[j];
                j++;
                k++;
            }
            j++;
        }
        
        int contador = 0;
        for(int i = 0; i < quantIngr; i++){
            for (int j = 0; j < n; j++){
                if (strcmp(ingredientes[i], tipicos[j])){
                    contador++;
                }
            }
        }
        
        if (contador >= n/2){
            printf("porcao tipica");
        }
    }
    
    return 0;
}