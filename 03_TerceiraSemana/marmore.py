# 1025 - Onde está o mármore

import sys


def main():
    resultados = []
    i = 1
    while True:
        numeros_marmore = []
        consultas = []
        n, q = map(int, sys.stdin.readline().split())
        if n == 0:
            break
        for _ in range(n):
            num = int(sys.stdin.readline())
            numeros_marmore.append(num)
        for _ in range(q):
            consulta = int(sys.stdin.readline())
            consultas.append(consulta)
        resultados.append(f'CASE# {i}:')
        i += 1
        numeros_marmore_pos = {}
        for idx, num in enumerate(sorted(numeros_marmore)):
            if num not in numeros_marmore_pos:
                numeros_marmore_pos[num] = idx + 1

        for c in consultas:
            if c in numeros_marmore_pos:
                resultados.append(f'{c} found at {numeros_marmore_pos[c]}')
            else:
                resultados.append(f'{c} not found')

    print('\n'.join(resultados))


if __name__ == '__main__':
    main()