class Filas:
    def __init__(self, capacidade):
        self.inicio = 0
        self.final = -1
        self.elementos = 0
        self.capacidade = capacidade
        self.valores = [None] * capacidade
    
    def filaCheia(self):
        print(f"fila cheia: {self.elementos == self.capacidade}")
    
    def filaVazia(self):
        print(f"fila vazia: {self.elementos == 0}")

    def enfileirar(self, valor):
        if self.elementos == self.capacidade:
            print("fila cheia")
            return
        elif self.final == self.capacidade -1: #circular
            self.final = -1
        self.final = self.final + 1
        self.valores[self.final] = valor
        self.elementos = self.elementos + 1    

    def desenfileirar(self):
        if self.elementos == 0:
            print("Lista vazia")
            return
        temp = self.valores[self.inicio]     
        self.inicio = self.inicio +1
        if self.inicio == self.capacidade: #circular
            self.inicio = 0
        self.elementos = self.elementos -1
        return temp
    
    def verPrimeiro(self):
        if self.elementos == 0:
            return -1
        print(f"{self.valores[self.inicio]}")
        
Meunome = Filas(7)
Meunome.enfileirar("E")
Meunome.enfileirar("D")
Meunome.enfileirar("U")
Meunome.enfileirar("A")
Meunome.enfileirar("R")
Meunome.enfileirar("D")
Meunome.enfileirar("O")

Meunome.verPrimeiro()

Meunome.desenfileirar()
Meunome.desenfileirar()
Meunome.desenfileirar()

Meunome.verPrimeiro()   