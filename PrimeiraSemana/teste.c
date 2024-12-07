#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    // Lê os ingredientes típicos
    int n, m;
    scanf("%i", &n);
    char tipicos_temp[n * 50];
    fgets(tipicos_temp, sizeof(tipicos_temp), stdin); // Leitura segura
    
    char tipicos[n][50];
    int j = 0, k = 0;
    for (int i = 0; i < n; i++) {
        k = 0;
        while (tipicos_temp[j] != ' ' && tipicos_temp[j] != '\0' && tipicos_temp[j] != '\n') {
            tipicos[i][k++] = tipicos_temp[j++];
        }
        tipicos[i][k] = '\0'; // Finaliza a string
        j++; // Avança após o espaço
    }

    scanf("%i", &m);

    for (int i = 0; i < m; i++) {
        char nomePorcao[50];
        int quantIngr;
        scanf("%s %i", nomePorcao, &quantIngr);

        char ingredientes_temp[quantIngr * 50];
        fgets(ingredientes_temp, sizeof(ingredientes_temp), stdin);

        char ingredientes[quantIngr][50];
        j = 0;
        for (int i = 0; i < quantIngr; i++) {
            k = 0;
            while (ingredientes_temp[j] != ' ' && ingredientes_temp[j] != '\0' && ingredientes_temp[j] != '\n') {
                ingredientes[i][k++] = ingredientes_temp[j++];
            }
            ingredientes[i][k] = '\0'; // Finaliza a string
            j++; // Avança após o espaço
        }

        // Conta ingredientes típicos
        int contador = 0;
        for (int i = 0; i < quantIngr; i++) {
            for (int j = 0; j < n; j++) {
                if (strcmp(ingredientes[i], tipicos[j]) == 0) {
                    contador++;
                }
            }
        }

        // Define se a porção é típica ou comum
        if (contador > quantIngr / 2) {
            printf("porcao tipica\n");
        } else {
            printf("porcao comum\n");
        }
    }

    return 0;
}
