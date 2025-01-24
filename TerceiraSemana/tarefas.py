# 704 Arrumando as Tarefas
# bits à deriva
# Samuel Guimarães Silva
# João Guilherme Alves
# Caio Vinicius da Cruz Coelho

import copy

def main():
    while True:
        try:
            valor_perdido = 0;

            tarefas = []
            N, H = input("").split()
            N = int(N)
            H = int(H)
            for i in range(N):
                v, t = input("").split()
                v = int(v)
                t = int(t)
                tarefas.append((v,t))

            tarefas.sort(key=lambda tup: (-tup[0], tup[1]))

            tarefas1 = []
            for i in range(H):
                tarefas1.append(tarefas[i])
            tarefas1.sort(key=lambda tup: tup[1])

            for i in range (H, N):
                tarefas1.append(tarefas[i])

            k = 0
            l = 0

            #print (horarios)
            print(valor_perdido)
            #print(tarefas)
        
        except EOFError:
            break

if __name__ == '__main__':
    main()