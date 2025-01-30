from numpy import ones,vstack
from numpy.linalg import lstsq
import sympy

i = int(input(''))

todas_coord = []
coord_est = []

for j in range(i):
    for k in range(4):
        linha_est = []
        ex, ey = input('').split()
        linha_est.append(float(ex))
        linha_est.append(float(ey))
        coord_est.append(linha_est.copy())
        linha_est.clear()
    todas_coord.append(coord_est.copy())
    coord_est.clear()


for j in range(i):

    #pontos das estrelas
    estrela1 = [(todas_coord[j][0][0],todas_coord[j][0][1]),(todas_coord[j][2][0],todas_coord[j][2][1])]
    estrela2 = [(todas_coord[j][1][0],todas_coord[j][1][1]),(todas_coord[j][3][0],todas_coord[j][3][1])]

    #equação estrela 1
    x_estrela1, y_estrela1 = zip(*estrela1)
    A = vstack([x_estrela1,ones(len(y_estrela1))]).T
    m1, c1 = lstsq(A, y_estrela1)[0]
    #print("A solução da equação da estrela 1 é: y={m1}x+{c1}".format(m1=m1,c1=c1))

    #equação estrela 2
    x_estrela2, y_estrela2 = zip(*estrela2)
    A = vstack([x_estrela2,ones(len(y_estrela2))]).T
    m2, c2 = lstsq(A, y_estrela2)[0]
    #print("A solução da equação da estrela 1 é: y={m2}x+{c2}".format(m2=m2,c2=c2))

    #perpendicular estrela1
    ponto_medio_1 = (((estrela1[0][0]+estrela1[1][0])/2), ((estrela1[0][1]+estrela1[1][1])/2))
    mp1 = (m1/(m1*m1))*-1
    cp1 = (mp1*ponto_medio_1[0]*-1)+ponto_medio_1[1]
    #print("A perpendicular da estrela 2 é: y={mp1}x+{cp1}".format(mp1=mp1,cp1=cp1))

    #perpendicular estrela2
    ponto_medio_2 = (((estrela2[0][0]+estrela2[1][0])/2), ((estrela2[0][1]+estrela2[1][1])/2))
    mp2 = (m2/(m2*m2))*-1
    cp2 = (mp2*ponto_medio_2[0]*-1)+ponto_medio_2[1]

    #print("A perpendicular da estrela 2 é: y={mp2}x+{cp2}".format(mp2=mp2,cp2=cp2))

    #interseção (ponto do buraco negro)
    x, y = sympy.symbols('x y')
    eq1 = sympy.Eq(mp1*x + cp1 - y, 0)
    eq2 = sympy.Eq(mp2*x + cp2 - y, 0)

    resultado = sympy.solve((eq1, eq2), 
                (x, y))
    
    result_x = resultado.get('x')

    print (result_x)