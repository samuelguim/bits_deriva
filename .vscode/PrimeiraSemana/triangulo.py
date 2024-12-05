# 1795 - Triângulo Trinomial

n_linha = int(input())

linha = [1]
for i in range(n_linha):
    linha = [sum(t) for t in zip([0,0]+linha, [0]+linha+[0], linha+[0,0])]

print(sum(linha))