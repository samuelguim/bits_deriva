# 1609 - Contando Carneirinhos

import sys

def encontra_unicos(lista):
    return list(set(lista))

def main():
    resultado = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        qtd_carneirinhos = sys.stdin.readline()
        carneirinhos = sys.stdin.readline().split()
        carneirinhos_distintos = len(encontra_unicos(carneirinhos))
        resultado.append(carneirinhos_distintos)


    print('\n'.join(map(str,resultado)))

if __name__ == '__main__':
    main()