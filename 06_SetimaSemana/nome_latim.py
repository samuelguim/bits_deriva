MOD = 10**9 + 7  

def fatorial(n, mod):
    resultado = 1
    for i in range(1, n + 1):
        resultado = (resultado * i) % mod
    return resultado

def contar_anagramas(palavra):
    from collections import Counter  
    tamanho = len(palavra)
    contador = Counter(palavra)  
    denominador = 1
    for quantidade in contador.values():
        if quantidade > 1:
            denominador = (denominador * fatorial(quantidade, MOD)) % MOD

    numerador = fatorial(tamanho, MOD)

    return (numerador * pow(denominador, MOD - 2, MOD)) % MOD

def main():
    import sys
    for linha in sys.stdin:
        palavra = linha.strip() 
        if palavra: 
            print(contar_anagramas(palavra))

if __name__ == "__main__":
    main()