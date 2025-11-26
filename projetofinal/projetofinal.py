# ============================================================
#   ETAPA 3 - IMPLEMENTAÇÃO DO GRAFO USANDO LISTA DE ADJACÊNCIA
# ============================================================

# Cada chave representa uma cidade
# Cada valor é uma lista de tuplas (Vizinho, Distância)

grafo = {
    "CRICIUMA": [("ICARA", 4), ("RINCAO", 8)],
    "ICARA": [("CRICIUMA", 4), ("TUBARAO", 8), ("RINCAO", 11)],
    "TUBARAO": [("ICARA", 8), ("SIDEROPOLIS", 7), ("NOVA VENEZA", 2)],
    "SIDEROPOLIS": [("TUBARAO", 7), ("ORLEANS", 9), ("ARARANGUA", 14)],
    "NOVA VENEZA": [("TUBARAO", 2), ("RINCAO", 7), ("ARARANGUA", 4), ("JAGUARUNA", 6)],
    "RINCAO": [("CRICIUMA", 8), ("ICARA", 11), ("NOVA VENEZA", 7), ("JAGUARUNA", 1)],
    "JAGUARUNA": [("RINCAO", 1), ("NOVA VENEZA", 6), ("ARARANGUA", 2)],
    "ARARANGUA": [("JAGUARUNA", 2), ("NOVA VENEZA", 4), ("SIDEROPOLIS", 14), ("ORLEANS", 10)],
    "ORLEANS": [("SIDEROPOLIS", 9), ("ARARANGUA", 10)]
}



# ============================================================
#       ETAPA 4 - ALGORITMO DE DIJKSTRA (FORMA DIDÁTICA)
# ============================================================

def dijkstra(grafo, origem):
    # 1. Distância inicial infinita para todos
    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[origem] = 0  # Origem = 0

    # 2. Conjunto de visitados
    visitados = set()

    # 3. Continua até visitar todos os nós
    while len(visitados) < len(grafo):

        # Selecionar o nó NÃO visitado com menor distância
        menor_no = None
        menor_distancia = float('inf')

        for cidade in grafo:
            if cidade not in visitados and distancias[cidade] < menor_distancia:
                menor_no = cidade
                menor_distancia = distancias[cidade]

        visitados.add(menor_no)

        # 4. Para cada vizinho do nó atual, tenta atualizar distâncias
        for vizinho, peso in grafo[menor_no]:
            nova_distancia = distancias[menor_no] + peso

            # Se encontrou um caminho melhor, atualiza
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia

    return distancias



# ============================================================
#           EXECUTANDO O DIJKSTRA A PARTIR DE CRICIÚMA
# ============================================================

resultado = dijkstra(grafo, "ICARA")

print("Menor distância da transportadora (CRICIUMA)\npara cada cidade:\n")
for cidade, distancia in resultado.items():
    print(f"{cidade}: {distancia}")
