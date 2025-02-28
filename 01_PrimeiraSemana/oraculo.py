# 1457 - Oráculo de Alexandria

def k_fatorial(n,k):
    result = n
    incremento = k
    while (n-k) >= 1:
        result *= n-k
        k += incremento
    return result


n_instancias = int(input())
resposta = []
for i in range(n_instancias):
    entrada = input()
    valor = int(''.join(n for n in entrada if n.isdigit()))
    k = entrada.count('!')
    resultado = k_fatorial(valor,k)
    resposta.append(resultado)


for r in resposta:
    print(r)
