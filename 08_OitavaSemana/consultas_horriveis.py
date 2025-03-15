ft1 = []
ft2 = []


def update(ft, n, index, valor):
    while index <= n:
        ft[index] += valor
        index += index & -index


def range_update(n, inicio, fim ,valor):
    update(ft1,n,inicio,valor)
    update(ft1,n,fim+1,-valor)
    update(ft2,n,inicio,valor*(inicio-1))
    update(ft2,n,fim+1,-valor*fim)


def point_query(ft, index):
    s = 0 
    while index > 0:
        s += ft[index]
        index -= index & (-index)
    return s


def query(i):
    return point_query(ft1, i) * i - point_query(ft2, i)


def range_soma(inicio, fim):
    return query(fim) - query(inicio-1)



def main():
    resultados = []
    global ft1, ft2
    consultas = int(input())
    for _ in range(consultas):
        n, c = map(int, input().split())

        ft1 = [0] * (n+1)
        ft2 = [0] * (n+1)
        for _ in range(c):
            comando = list(map(int, input().split()))
            if comando[0] == 0:
                range_update(n, comando[1], comando[2], comando[3])
            else:
                resultados.append(range_soma(comando[1], comando[2]))
    print('\n'.join(map(str,resultados)))


if __name__ == '__main__':
    main()