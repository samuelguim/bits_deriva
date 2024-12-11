# 1023 - Estiagem

import math
import sys

def get_cidade_string(c_por_p, p, c, i):
    linha = " ".join([f"{v}-{k}" for k, v in c_por_p.items()])
    consumo_medio = math.floor((100 * c)/p)/100
    string = f'Cidade# {i}:\n{linha}\nConsumo medio: {consumo_medio:.2f} m3.\n'
    return string


def main():
    index = 1
    resultados = []
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        consumo_por_pessoa = {}
        total_moradores = 0
        total_cosumo = 0

        for _ in range(n):
            qtd_moradores, consumo = map(int, sys.stdin.readline().split())
            total_moradores += qtd_moradores
            total_cosumo += consumo
            key = consumo // qtd_moradores
            consumo_por_pessoa[key] = consumo_por_pessoa.get(key, 0) + qtd_moradores

        consumo_por_pessoa = dict(sorted(consumo_por_pessoa.items()))
        
        resultados.append(get_cidade_string(consumo_por_pessoa, total_moradores, total_cosumo, index))
        index += 1


    print('\n'.join(resultados), end='')

if __name__ == '__main__':
    main()