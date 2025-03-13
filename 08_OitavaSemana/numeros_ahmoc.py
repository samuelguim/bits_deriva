def kmpAlgorithm(string, pattern):
    LPSArr = buildLPSArr(pattern)
    return stringMatching(string, pattern, LPSArr)

def buildLPSArr(pattern):
    LPSArr = [-1]*len(pattern)

    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            LPSArr[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = LPSArr[j-1] + 1
        else:
            i += 1
    return LPSArr

def stringMatching(string, pattern, LPSArr):
    i, j = 0, 0
    while i + len(pattern) - j <= len(string):
        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = LPSArr[j-1] + 1
        else:
            i += 1
    return False

def main():
    instancia = 1
    while True:
        padrao = input()

        if padrao == "0":
            return False
        
        txt = input()

        resultado = kmpAlgorithm(txt, padrao)

        if resultado == True:
            print(f"Instancia {instancia}")
            print("verdadeira\n")
        elif resultado == False:
            print(f"Instancia {instancia}")
            print("falsa\n")
        instancia += 1

if __name__ == "__main__":
    main()