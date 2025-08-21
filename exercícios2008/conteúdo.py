class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valor = [None] * capacidade

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('vetor cheio')
        else:
            self.ultima_posicao += 1
            self.valor[self.ultima_posicao] = valor


    def imprimir(self):
        if self.ultima_posicao == -1:
            print('vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-',self.valor[i])

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            print(f'Verificando índice: {i}')
            if valor == self.valor[i]:
                print(f'Valor {valor} encontrado no índice {i}')
                return i
        print(f'Valor {valor} não encontrado')
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range (posicao, self.ultima_posicao):
                self.valor[i] = self.valor[i+1]
            self.ultima_posicao = self.ultima_posicao - 1


vetor = VetorNaoOrdenado(4)
vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(4)
vetor.inserir(5)  # Vai mostrar "vetor cheio"

vetor.imprimir() # mostra o que há dentro do vetor
vetor.pesquisar(2)

vetor.excluir(3)
vetor.imprimir()

