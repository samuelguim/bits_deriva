from collections import deque

def palavras(setA, setB):
    visited = set()
    queue = deque()

    for a in setA:
        for b in setB:
            queue.append((a, b))
    
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == b:
            return 'S'
        
        if a.startswith(b):
            for bnext in setB:
                queue.append((a[len(b):], bnext))
    
        if b.startswith(a):
            for anext in setA:
                queue.append((anext, b[len(a):]))

    return 'N'




def main():
    resposta = []
    try:
        while True:
            n1, n2 = map(int, input().split())
            setA = [input().strip() for _ in range(n1)]
            setB = [input().strip() for _ in range(n2)]
            resposta.append(palavras(setA, setB))
    except EOFError:
        pass
    print('\n'.join(resposta))




if __name__ == '__main__':
    main()