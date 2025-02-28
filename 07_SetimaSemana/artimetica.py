def main():
    resultados = []
    while True:
        
        num1, num2 = map(int, input().split())
        if num1 == 0 and num2 == 0:
            break
        qtd_carry = calcula_carry(num1, num2)
        if qtd_carry == 1:
            resultados.append('1 carry operation.')
        elif qtd_carry > 0:
            resultados.append(f'{qtd_carry} carry operations.')
        else:
            resultados.append('No carry operation.')
    print('\n'.join(map(str, resultados)))





def calcula_carry(n1, n2):
    count = 0
    carry = 0
    while n1 > 0 or n2 > 0:
        ultimo1 = n1 % 10
        ultimo2 = n2 % 10
        if ultimo1 + ultimo2 + carry > 9:
            carry = 1
            count += 1
        else:
            carry = 0
        n1 = n1 // 10
        n2 = n2 // 10
    return count


if __name__ == '__main__':
    main()