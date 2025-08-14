









""" class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionarLivro(self):
        pass
    
    def exibirLivrosDisponíveis(self):
        pass

class Livro:
    def __init__(self, codigo, titulo, autor, disponivel):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def exibirDetalhes(self):
         print(f"{self.titulo}")
         print(f"{self.autor}")
         print(f"{self.disponivel}")
        
class Usuario:
    def __init__(self, nome, livrosEmprestados):
        self.nome = nome
        self.livrosEmprestados = livrosEmprestados

    def emprestarLivro(self):
        pass

    def devolverLivro(self):
        pass



#inicio
bibliotecasatc = Biblioteca("satc")

while True:
    print("------------------------------------------- ")
    print(" Diga qual opção deseja:                    ")
    print(" 1 - cadastrar livro                        ")
    print(" 2 - exibir livros disponiveis para locação ")
    print(" 3 - locar livro                            ")
    print(" 4 - devolver livro                         ")
    print(" 5 - exibir detalhes de um livro específico ")
    op = int(input(" Digite a opção desejada: "))


    while (op > 0 or op < 6):
        if op == 1:
            print("cadastre seu livro: ")
            codigoLivro = input("digite o codigo do livro: ")
            nomeLivro = input("digite o nome do livro: ")
            nomeAutor = input("digite o nome do autor: ")
            print("O livro consta como disponível pois acabou de ser criado!")
            novolivro = Livro(codigoLivro, nomeLivro, nomeAutor, True) 
            bibliotecasatc.adicionarLivro(novolivro)
        
        elif op == 2:
            print("estes são os livros disponíveis para locação: ") """
