# 2004 - Enisvaldo com Fome

n = int(input())

for _ in range(n):
    alimentos = {}
    gramas = 0
    qtd_alimentos_diferentes = int(input())
    for i in range(qtd_alimentos_diferentes):
        alimento = tuple(map(int, input().split()))
        alimentos[alimento[0]] = alimentos.get(alimento[0], []) + [alimento[1]]

        if i == qtd_alimentos_diferentes-1:
            for key in alimentos:
                gramas_otimizadas = max([item for item in alimentos[key] if item <= 100 and item >= 10], default=0)
                if gramas_otimizadas == 0:
                    gramas += max([item for item in alimentos[key]])
                else:
                    gramas += gramas_otimizadas
                

    print(gramas)
