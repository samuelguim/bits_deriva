#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
 
bool estaNasCartas(int a, int b[5]){
    if (a != b[0] && a != b[1] && a != b[2] && a != b[3] && a != b[4]){
        return false;
    }
    else {
        return true;
    }
}

int main() {
    int cartas[5];
    int comparacao[5] = {0,0,0,0,0};
    char input[16];

    while(1){
        //leitura
        scanf(" %[^\n]s", input);

        if(strcmp(input, "0 0 0 0 0") == false){
            break;
        }
        
        // transforma a string da entrada em uma lista de inteiros
        int j = 0;
        for (int i = 0; i < 5; i++){
            char temp[3] = "  ";
            int k = 0;
            while (isdigit(input[j]))
            {
                temp[k] = input[j];
                k++; 
                j++;
            }
            j++;
            cartas[i] = atoi(temp);
        }
        
        //organiza cartas
        int menorPrincipe;
        int maiorPrincipe;
        int cartasPrincesa[2];
        int temp;
        cartasPrincesa[0] = cartas[0];
        cartasPrincesa[1] = cartas[1];
        cartasPrincesa[2] = cartas[2];

        if (cartasPrincesa[0] > cartasPrincesa[2]){
            temp = cartasPrincesa[0];
            cartasPrincesa[0] = cartasPrincesa[2];
            cartasPrincesa[2] = temp;}

        if (cartasPrincesa[0] > cartasPrincesa[1]){
            temp = cartasPrincesa[0];
            cartasPrincesa[0] = cartasPrincesa[1];
            cartasPrincesa[1] = temp;}

        if (cartasPrincesa[1] > cartasPrincesa[2]){
            temp = cartasPrincesa[1];
            cartasPrincesa[1] = cartasPrincesa[2];
            cartasPrincesa[2] = temp;}
        int medianaPrincesa = cartasPrincesa[1];
        int maiorPrincesa = cartasPrincesa [2];
        
        if (cartas[3] < cartas[4]){
            menorPrincipe = cartas[3];
            maiorPrincipe = cartas[4];
        }
        else {
            menorPrincipe = cartas[4];
            maiorPrincipe = cartas[3];
        }

        // resultados
        int resultado;

        if (menorPrincipe > maiorPrincesa){
            resultado = 1;
            while (estaNasCartas(resultado, cartas))
            {
                resultado++;
            }
            if (resultado <= 52){
                printf ("%d\n", resultado);
            }
            else{
                resultado = -1;
                printf ("%d\n", resultado);
            }
        }

        else if (menorPrincipe > medianaPrincesa){
            resultado = medianaPrincesa+1;
            while (estaNasCartas(resultado, cartas))
            {
                resultado++;
            }
            if (resultado <= 52){
                printf ("%d\n", resultado);
            }
            else{
                resultado = -1;
                printf ("%d\n", resultado);
            }
        }

        else if (menorPrincipe < medianaPrincesa){
            if (maiorPrincipe > maiorPrincesa){
                resultado = maiorPrincesa+1;
                while (estaNasCartas(resultado, cartas))
                {
                    resultado++;
                }
                if (resultado <= 52){
                    printf ("%d\n", resultado);
                }
                else{
                    resultado = -1;
                    printf ("%d\n", resultado);
                }
            }
            else{
                resultado = -1;
                printf ("%d\n", resultado);
            }  
        }
    }
    return 0;
}