class Livro: #cria a classe livro
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # por padrão deixa livro disponivel

    def exibirDetalhes(self): #exibe os de talher do livro
        print(f'Título: {self.titulo}, Autor: {self.autor}, Disponível: {"Sim" if self.disponivel else "Não"}') # se o livro esta disponivel print sim, else nao

# cria a classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []  #cria lista de livros emprestados

    def emprestarLivro(self, livro):
        if livro.disponivel: # se esta disponivel
            livro.disponivel = False   # deixa ele indisponivel
            self.livrosEmprestados.append(livro) # adiciona o livro na lista de emprestados
            print(f'{self.nome} emprestou o livro: {livro.titulo}') #só printa oque aconteceu
        else:
            print(f'O livro "{livro.titulo}" não está disponível.')

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados: # se ele esta nos livros emprestados
            livro.disponivel = True   # devolve ele, deixa ele disponivel
            self.livrosEmprestados.remove(livro) # remove da lista de emprestados
            print(f'{self.nome} devolveu o livro: {livro.titulo}')
        else:
            print(f'{self.nome} não tem o livro "{livro.titulo}" emprestado.')


class Biblioteca: # cria classe biblioteca
    def __init__(self, nome):
        self.nome = nome
        self.livros = []  #cria a lista de livros

    def adicionarLivro(self, livro):
        self.livros.append(livro)#adiciona o livro a lista
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

    def exibirLivrosDisponiveis(self):
        print(f'\nLivros disponíveis na Biblioteca {self.nome}:')
        for livro in self.livros: # para o livro na lista de livros
            if livro.disponivel: # se o livro é disponivel
                livro.exibirDetalhes()

livro1 = Livro("teste", "thierry")
livro2 = Livro("O Senhor dos Anéis", "algum autor")
livro3 = Livro(" turma da monica", "mauricio de souza")

usuario1 = Usuario("dudu")
usuario2 = Usuario("tutu")

biblioteca = Biblioteca("Biblioteca satc")


biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)


biblioteca.exibirLivrosDisponiveis()


usuario1.emprestarLivro(livro1)
usuario2.emprestarLivro(livro2)


biblioteca.exibirLivrosDisponiveis()

usuario1.devolverLivro(livro1)


biblioteca.exibirLivrosDisponiveis()
