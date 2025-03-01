#2674 Super Primos: Ativar!
# bits à deriva
# Samuel Guimarães Silva
# João Guilherme Alves
# Caio Vinicius da Cruz Coelho

import math
import sys

def main():
    resposta = []
    while True:
        try:
            linha = sys.stdin.readline()
            if linha == '' or linha == '\n':
                break
            num = int(linha)
            digitos = [int(d) for d in str(num)]
            if is_primo(num):
                if all(list(map(is_primo, digitos))):
                    resposta.append('Super')
                else:
                    resposta.append('Primo')
            else:
                resposta.append('Nada')
        except EOFError:
            break
    
    print('\n'.join(resposta))



def is_primo(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
    main()

