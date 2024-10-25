class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  
        self.grupos = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.grupos -= 1  
    
    def verificar(self, x, y):
        return self.find(x) == self.find(y)
    
    def contarGrupos(self):
        return self.grupos

# Ejemplo de uso
n = 10
uf = UnionFind(n)
uf.union(1, 2)
uf.union(3, 4)
uf.union(2, 3)
print(uf.verificar(1, 4))  
print(uf.contarGrupos())   