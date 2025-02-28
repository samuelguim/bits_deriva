# 1211 - Lista Telefônica Econômica
import sys

def encontra_prefixo(num1, num2):
    count = 0
    for n1, n2 in zip(num1, num2):
         if n1 == n2:
            count += 1
         else:
            break
    return count


def main():
    resultados = []
    while True:
        try:
            valor = sys.stdin.readline()
            if valor == '\n' or valor == '':
                break
            n = int(valor)
            numeros = []
            contador = 0
            for _ in range(n):
                numero = sys.stdin.readline()
                numeros.append(numero[:-1])

            numeros = sorted(numeros)
            for i in range(len(numeros) - 1):
                contador += encontra_prefixo(numeros[i], numeros[i+1])
                
            resultados.append(contador)
            
        except EOFError:
            break

    print('\n'.join(map(str,resultados)))


if __name__ == '__main__':
    main()




