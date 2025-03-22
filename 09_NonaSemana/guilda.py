class UnionFind:
    def __init__(self, tamanho, pontos):
        self.pai = list(range(tamanho))
        self.rank = [1] * tamanho
        self.soma_pontos = pontos[:]

    def find(self, p):
        if self.pai[p] != p:
            self.pai[p] = self.find(self.pai[p])
        return self.pai[p]

    def union(self, p, q):
        raizP = self.find(p)
        raizQ = self.find(q)

        if raizP != raizQ:
            if self.rank[raizP] > self.rank[raizQ]:
                self.pai[raizQ] = raizP
                self.soma_pontos[raizP] += self.soma_pontos[raizQ]
            elif self.rank[raizP] < self.rank[raizQ]:
                self.pai[raizP] = raizQ
                self.soma_pontos[raizQ] += self.soma_pontos[raizP]
            else:
                self.pai[raizQ] = raizP
                self.soma_pontos[raizP] += self.soma_pontos[raizQ]
                self.rank[raizP] += 1

    def get_soma_pontos(self, p):
        return self.soma_pontos[self.find(p)]


def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        pontos = list(map(int, input().split()))

        uf = UnionFind(N, pontos)
        vitorias = 0

        for _ in range(M):
            Q, A, B = map(int, input().split())
            A -= 1
            B -= 1

            if Q == 1:
                uf.union(A, B)
            elif Q == 2:
                if uf.get_soma_pontos(A) > uf.get_soma_pontos(B) and uf.find(0) == uf.find(A):
                    vitorias += 1
                elif uf.get_soma_pontos(B) > uf.get_soma_pontos(A) and uf.find(0) == uf.find(B):
                    vitorias += 1

        print(vitorias)


if __name__ == "__main__":
    main()