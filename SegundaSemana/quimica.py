

def confereInicial(sequencia, i, j):
    substancia = sequencia[i][j]
    for i in range(len(sequencia)):
        if substancia == sequencia[i][2]:
            return False
            break
    return True

def procuraLinhaSubstancia(sequencia, i, j):
    for i2 in range (R):
        if sequencia[i][j] == sequencia [i2][2]:
            return i2
    
def reacoes(sequencia, nivel, i, j):
    if confereInicial(sequencia, i, j) == False:
        nivelReacao.append(nivel)
        nivel+=1
        if confereInicial(sequencia, i, 0) == False:
            i1 = procuraLinhaSubstancia(sequencia, i, 0)
        else:
            i1 = i
        if confereInicial(sequencia, i, 1) == False:
            i2 = procuraLinhaSubstancia(sequencia, i, 1)
        else:
            i2 = i
        reacoes (sequencia, nivel, i1, 0)
        reacoes (sequencia, nivel, i2, 1)

R = 1
nivelReacao = []

while (R != 0):
    nivelReacao.clear()
    R = int(input(''))
    if (R > 0):
        linhas, colunas = (R, 3)
        sequencia = [[0]*colunas]*linhas

        #recebe os dados iniciais
        for i in range(R):
            stringLinha = input('').replace(' + ', ' ').replace(' -> ', ' ').split()
            sequencia [i] = stringLinha
        reacoes(sequencia, 0, R-1, 2)
        print (sequencia[R-1][2], 'requires', len(nivelReacao), 'containers')
