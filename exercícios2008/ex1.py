class VetorDesordanado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.Nome = [None] * capacidade

    def inserir(self, Nome):
        if self.ultima_posicao == self.capacidade - 1:
            print('vetor cheio')
        else:
            self.ultima_posicao += 1
            self.Nome[self.ultima_posicao] = Nome


    def imprimir(self):
        if self.ultima_posicao == -1:
            print('vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-',self.Nome[i])

    def pesquisar(self, Nome):
        for i in range(self.ultima_posicao + 1):
            print(f'Verificando índice: {i}')
            if Nome == self.Nome[i]:
                print(f'Nome {Nome} encontrado no índice {i}')
                return i
        print(f'Nome {Nome} não encontrado')
        return -1
    
    def excluir(self, Nome):
        posicao = self.pesquisar(Nome)
        if posicao == -1:
            return -1
        else:
            for i in range (posicao, self.ultima_posicao):
                self.Nome[i] = self.Nome[i+1]
                
            self.ultima_posicao = self.ultima_posicao - 1


Meunome = VetorDesordanado(7) #Letras do meu nome
Meunome.inserir("E")
Meunome.inserir("D")
Meunome.inserir("U")
Meunome.inserir("A")
Meunome.inserir("R")
Meunome.inserir("D")
Meunome.inserir("O")

Meunome.imprimir()

Meunome.pesquisar("O")
Meunome.pesquisar("E")
Meunome.pesquisar("A")

Meunome.excluir("O")
Meunome.excluir("E")
Meunome.excluir("A")

Meunome.imprimir()






