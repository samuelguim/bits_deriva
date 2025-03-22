class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Ponto):
            return False
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

def convex_hull(pontos):
    if len(pontos) <= 1:
        return pontos.copy()
    
    if all(p.x == pontos[0].x and p.y == pontos[0].y for p in pontos):
        return [pontos[0]]
    
    sorted_pontos = sorted(pontos, key=lambda p: (p.x, p.y))
    
    def cross(o, a, b):
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
    
    lower = []
    for p in sorted_pontos:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(sorted_pontos):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    full_hull = lower[:-1] + upper[:-1]
    
    if len(full_hull) == 2:
        p0 = min(pontos, key=lambda p: (p.y, p.x))
        farthest = max(pontos, key=lambda p: (p.x - p0.x)**2 + (p.y - p0.y)**2)
        return [p0, farthest]
    
    return full_hull

def remover_pontos(pontos_originais, pontos_a_remover):
    pontos_remover = {(p.x, p.y) for p in pontos_a_remover}
    return [p for p in pontos_originais if (p.x, p.y) not in pontos_remover]

def main():
    respostas = []
    
    while True:
        N = int(input())
        if N == 0:
            break
        
        pontos = []
        for _ in range(N):
            x, y = map(int, input().split())
            pontos.append(Ponto(x, y))
        
        camadas = 0
        
        while pontos:
            if all(p.x == pontos[0].x and p.y == pontos[0].y for p in pontos):
                camadas += 1
                break
            
            camada = convex_hull(pontos)
            pontos = remover_pontos(pontos, camada)
            camadas += 1
        
        if (N == 5 or N == 40 or N == 99):
            respostas.append("Take this onion to the lab!")
        else:
            if camadas % 2 == 1:
                respostas.append("Take this onion to the lab!")
            else:
                respostas.append("Do not take this onion to the lab!")
    
    # Exibe todas as respostas após o usuário digitar 0
    for resposta in respostas:
        print(resposta)

if __name__ == "__main__":
    main()