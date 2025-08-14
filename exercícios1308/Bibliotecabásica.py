# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Por padrão, o livro está disponível

    def exibirDetalhes(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}, Disponível: {"Sim" if self.disponivel else "Não"}')

# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []  # Lista de livros emprestados pelo usuário

    def emprestarLivro(self, livro):
        if livro.disponivel:
            livro.disponivel = False  # Marca o livro como não disponível
            self.livrosEmprestados.append(livro)
            print(f'{self.nome} emprestou o livro: {livro.titulo}')
        else:
            print(f'O livro "{livro.titulo}" não está disponível.')

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True  # Marca o livro como disponível
            self.livrosEmprestados.remove(livro)
            print(f'{self.nome} devolveu o livro: {livro.titulo}')
        else:
            print(f'{self.nome} não tem o livro "{livro.titulo}" emprestado.')

# Classe Biblioteca
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []  # Lista de livros na biblioteca

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

    def exibirLivrosDisponiveis(self):
        print(f'\nLivros disponíveis na Biblioteca {self.nome}:')
        for livro in self.livros:
            if livro.disponivel:
                livro.exibirDetalhes()

# Fluxo principal
# Criando instâncias das classes Livro, Usuario e Biblioteca
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro3 = Livro("A Metamorfose", "Franz Kafka")

usuario1 = Usuario("João")
usuario2 = Usuario("Maria")

biblioteca = Biblioteca("Biblioteca Central")

# Adicionando livros à biblioteca
biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)

# Exibindo livros disponíveis
biblioteca.exibirLivrosDisponiveis()

# Usuários emprestando livros
usuario1.emprestarLivro(livro1)
usuario2.emprestarLivro(livro2)

# Exibindo livros disponíveis após o empréstimo
biblioteca.exibirLivrosDisponiveis()

# Usuários devolvendo livros
usuario1.devolverLivro(livro1)

# Exibindo livros disponíveis após a devolução
biblioteca.exibirLivrosDisponiveis()
