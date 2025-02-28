while True:

    quant_numero, divisor = map(int, input().split())

    lista_numero = []

    if (quant_numero == 0 and divisor == 0):
        print(quant_numero, divisor)
        break

    for i in range(quant_numero):
        numero = int(input())
        lista_numero.append(numero)

    if any(x < 0 for x in lista_numero):
        resultado = sorted(lista_numero, key=lambda x: (x % divisor if x >= 0 else -(abs(x) % divisor)
                                                    ,0 if x % 2 != 0 else 1
                                                    ,-x if x % 2 != 0 else x
                                                    ,(x % divisor, x)))

    else:
        resultado = sorted(lista_numero, key=lambda x: (x % divisor if x % 2 == 0 else x % divisor
                                                    , -x if x % 2 != 0 else x
                                                    , (x % divisor, x)))
    
 
    print(quant_numero, divisor) 
    for i in range(quant_numero):
        print(resultado[i])