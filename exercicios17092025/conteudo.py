class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def mostraNo(self):
        print(f"no: {self.valor}")
        
class listaEncadeada:
    def __init__(self, ):
        self.primeiro = None
        
    def inserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def mostrar(self):
        if self.primeiro == None:
            print("erro de lista vazia")
            return None
        atual = self.primeiro
        while atual != None:
            atual.mostraNo()
            atual = atual.proximo
    
    def excluirInicio(self):
        if self.primeiro == None:
            print("Erro de lista vazia")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    
    def pesquisar(self, valor):
        if self.primeiro == None:
            print("Erro de lista vazia")
            return None
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual
    
    def excluirPosicao(self, valor):
        if self.primeiro == None:
            print("Erro de lista vazia")
            return None
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual
                

# Testando a lista encadeada

lista = listaEncadeada()

#A) Inserindo elementos no início
lista.inserirInicio("E")
lista.inserirInicio("D")
lista.inserirInicio("U")
lista.inserirInicio("A")
lista.inserirInicio("R")
lista.inserirInicio("D")
lista.inserirInicio("O")

# B) Mostrando a lista
lista.mostrar()

# C) Excluindo o primeiro elemento
lista.excluirInicio()

# D) Mostrando a lista após a exclusão
lista.mostrar()

#E
resultado = lista.pesquisar("E")
if resultado:
    print(f"Elemento encontrado: {resultado.valor}")
else:
    print("Elemento não encontrado.")

#F
lista.excluirPosicao("A")

#G
lista.mostrar()

