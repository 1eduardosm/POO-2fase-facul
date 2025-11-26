#   CLASSE GRAFO (LISTA DE ADJACÊNCIA)

class Grafo:
    def __init__(self):
        self.vertices = {}

    # Adiciona um vértice ao grafo
    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    # Adiciona uma aresta ponderada
    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.vertices[origem].append((destino, peso))
        self.vertices[destino].append((origem, peso))  # grafo não direcionado

    # Mostra o grafo
    def mostrar(self):
        for v in self.vertices:
            print(f"{v} -> {self.vertices[v]}")


#   CLASSE DIJKSTRA

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular(self, origem):
        # 1. Inicializa distâncias
        distancias = {v: float('inf') for v in self.grafo.vertices}
        distancias[origem] = 0

        # 2. Conjunto de visitados
        visitados = set()

        # 3. Enquanto não visitar todos
        while len(visitados) < len(self.grafo.vertices):

            # Escolhe o menor nó não visitado
            menor_no = None
            menor_dist = float('inf')

            for v in self.grafo.vertices:
                if v not in visitados and distancias[v] < menor_dist:
                    menor_no = v
                    menor_dist = distancias[v]

            visitados.add(menor_no)

            # Atualiza vizinhos (RELAXAMENTO)
            for vizinho, peso in self.grafo.vertices[menor_no]:
                nova_dist = distancias[menor_no] + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist

        return distancias


g = Grafo()

g.adicionar_aresta("CRICIUMA", "ICARA", 4)
g.adicionar_aresta("CRICIUMA", "RINCAO", 8)
g.adicionar_aresta("ICARA", "TUBARAO", 8)
g.adicionar_aresta("ICARA", "RINCAO", 11)
g.adicionar_aresta("TUBARAO", "SIDEROPOLIS", 7)
g.adicionar_aresta("TUBARAO", "ARARANGUA", 4)
g.adicionar_aresta("TUBARAO", "NOVA VENEZA", 2)
g.adicionar_aresta("NOVA VENEZA", "RINCAO", 7)
g.adicionar_aresta("NOVA VENEZA", "JAGUARUNA", 6)
g.adicionar_aresta("JAGUARUNA", "ARARANGUA", 2)
g.adicionar_aresta("ARARANGUA", "SIDEROPOLIS", 14)
g.adicionar_aresta("RINCAO", "JAGUARUNA", 1)
g.adicionar_aresta("ARARANGUA", "ORLEANS", 10)
g.adicionar_aresta("SIDEROPOLIS", "ORLEANS", 9)

d = Dijkstra(g)

origem = "CRICIUMA"
resultado = d.calcular(origem)

print(f"\nMenor distância a partir de {origem}:\n")
for cidade, distancia in resultado.items():
    print(f"{cidade}: {distancia}")
