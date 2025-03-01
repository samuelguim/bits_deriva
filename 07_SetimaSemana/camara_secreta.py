# 1839 A Câmara Secreta
# bits à deriva
# Samuel Guimarães Silva
# João Guilherme Alves
# Caio Vinicius da Cruz Coelho

def fatorial_ate(numero, parada):
    if numero == 0 or numero == 1:
        return 1
    
    fatorial = numero
    for i in range(1, parada):
        fatorial = fatorial * (numero - i)
    
    return fatorial

def main():
    respostas = []
    
    N, M = map(int, input().split())
    grid = []
    
    for i in range(N):
        grid.append(input())
    
    while True:
        try:
            xA, yA, xB, yB = map(int, input().split())
            
            comprimento = (xB - xA + 1)
            largura = (yB - yA + 1)
            tamanhoRegiao = comprimento * largura
            
            paredes = 0
            for i in range(yA-1, yB):
                for j in range(xA-1, xB):
                    if grid[j][i] == '#':
                        paredes += 1
            
            if paredes == 0:
                combinacoes = 0
            else:
                combinacoes = fatorial_ate(tamanhoRegiao, paredes) // fatorial_ate(paredes, paredes)
                combinacoes = (combinacoes - 1) % 1000000007
            
            respostas.append(combinacoes)
        
        except EOFError:
            break
    
    for resposta in respostas:
        print(resposta)

if __name__ == "__main__":
    main()