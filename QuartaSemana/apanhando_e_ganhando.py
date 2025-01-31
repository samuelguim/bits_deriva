# 1084 - Apagando e Ganhando


def main():

    resultados = []
    while True:
        n_digitos, qtd_apagar = map(int, input().split())
        if n_digitos == 0 and qtd_apagar == 0:
            break
        numero = input().strip()
        resposta = teste_pilha(numero, qtd_apagar)
        resultados.append(resposta)

    print('\n'.join(resultados))


def teste_pilha(num, n):
    pilha = []
    remocoes = 0
    for i in num:
        while len(pilha) > 0 and i > pilha[-1] and remocoes < n:
            pilha.pop()
            remocoes += 1
        pilha.append(i)

    while remocoes < n:
        pilha.pop()
        remocoes += 1


    return ''.join(pilha)



if __name__ == '__main__':
    main()


#4 2
#3579
#6 3
#123123
##6 1
#837125
#8 4
#95111451
#0 0