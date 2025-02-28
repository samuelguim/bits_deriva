# 1579 - Transporte de Painés Solares

def distribui(n_caminhoes: int, pesos: list, maximo: int):
    caminhoes_usados = 1
    carga_atual = 0

    for p in pesos:
        if carga_atual + p > maximo:
            caminhoes_usados += 1
            carga_atual = p 
            if caminhoes_usados > n_caminhoes:
                return False
        else:
            carga_atual += p
    return True



def minimiza_valor_maximo(n_caminhoes: int, pesos: list):
    low, high = max(pesos), sum(pesos)
    best = high

    while low <= high:
        mid = (low + high) // 2
        if distribui(n_caminhoes, pesos, mid):
            best = mid
            high = mid - 1
        else:
            low = mid + 1

    return best



def main():

    resultados = []
    n = int(input())
    for _ in range(n):
        n_paines, n_caminhoes, frete = map(int, input().split())
        peso_paines = list(map(int, input().split()))
        min_carga_max = minimiza_valor_maximo(n_caminhoes, peso_paines)
        resultados.append(f'{min_carga_max} ${min_carga_max * n_caminhoes * frete}')
    
    print('\n'.join(resultados))



if __name__ == '__main__':
    main()