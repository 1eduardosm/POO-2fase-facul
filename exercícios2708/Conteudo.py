class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [None] * capacidade

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Mensagem de vetor cheio')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                break
            posicao = i + 1

        # Desloca os valores para a direita
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('Mensagem de vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    def pesquisar(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while limite_inferior <= limite_superior:
            posicao_atual = (limite_inferior + limite_superior) // 2

            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif self.valores[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual - 1

        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print("Valor não encontrado")
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
