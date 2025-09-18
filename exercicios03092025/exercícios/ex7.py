class Pilhas:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = [None] * capacidade
    
    def pilhaCheia(self):
        print(f"pilha cheia {self.topo == self.capacidade -1}")
    
    def pilhaVazia(self):
        print(f"pilha vazia {self.topo == -1}")
    
    def empilhar(self, valor):
        if self.topo == self.capacidade -1:
            print("Pilha cheia")
        else:
            self.topo = self.topo + 1
        self.valores[self.topo] = valor
    
    def desempilhar(self):
        if self.topo == -1:
            print("Pilha vazia")
        else:
            self.topo = self.topo - 1
    
    def verTopo(self):
        if self.topo != -1:
            print(f"{self.valores[self.topo]}")
        else: 
            return -1
        
Meunome = Pilhas(7)

#a)
Meunome.desempilhar()

#b)
Meunome.empilhar("E")
Meunome.empilhar("D")
Meunome.empilhar("U")
Meunome.empilhar("A")
Meunome.empilhar("R")
Meunome.empilhar("D")
Meunome.empilhar("O")

#c)
Meunome.empilhar("X")

#d)
Meunome.verTopo()

#e)
Meunome.desempilhar()
Meunome.desempilhar()
Meunome.desempilhar()
Meunome.verTopo()   