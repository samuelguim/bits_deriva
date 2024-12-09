# 1068 - Balanço de Parênteses

def checa_balanco(exp, i, c):
    if i == len(exp):
        return c == 0
    
    if exp[i] == '(':
        c += 1
    
    if exp[i] == ')':
        c -= 1

    if c < 0:
        return False
    
    return checa_balanco(exp,i+1,c)



while True:
    try:
        expressao = input()
        if checa_balanco(expressao,0,0):
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break


    
