def bom_ruim(palavras):
    palavras.sort()
    for i in range(len(palavras) - 1):
        if palavras[i+1].startswith(palavras[i]):
            return False
    return True

def main():
    while True:
        N = int(input())
        if N == 0:
            break
        palavras = [input().strip() for i in range(N)]
        if bom_ruim(palavras):
            print("Conjunto Bom")
        else:
            print("Conjunto Ruim")

if __name__ == "__main__":
    main()