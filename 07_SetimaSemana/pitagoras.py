import math
import sys


def main():
    resultados = []
    while True:
        try:
            linha = sys.stdin.readline().split()
            if linha == [] or linha == '\n':
                break
            nums = list(map(int, linha))
            nums_ordenados = sorted(nums, reverse=True)
            mdc_numeros = math.gcd(math.gcd(nums_ordenados[0], nums_ordenados[1]), nums_ordenados[2])

            if nums_ordenados[0] ** 2 == nums_ordenados[1] ** 2 + nums_ordenados[2] ** 2:
                if mdc_numeros == 1:
                    resultados.append('tripla pitagorica primitiva')
                else:
                    resultados.append('tripla pitagorica')
            else:
                resultados.append('tripla')
        except EOFError:
            break
    print('\n'.join(resultados))









if __name__ == '__main__':
    main()