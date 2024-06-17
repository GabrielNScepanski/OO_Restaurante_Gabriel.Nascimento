# Classe Livro
class Livro:
    def __init__(self, registro, titulo, autor, ano_publicacao):
        self.registro = registro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def idade_livro(self, ano_atual):
        return ano_atual - self.ano_publicacao

    def emprestar(self):
        self.disponivel = False

# Classe Emprestimo
from datetime import date, timedelta

class Emprestimo:
    def __init__(self, livro, data_emprestimo):
        self.livro = livro
        self.data_emprestimo = data_emprestimo

    def dias_para_fim_quarentena(self):
        return (date.today() - self.data_emprestimo).days - 14

# Classe Aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.acervo = []
    
    def adicionar_livro(self, novo_livro):
        self.acervo.append(novo_livro)

# Exemplo de uso
biblioteca = Biblioteca()
livro1 = Livro(123, 'O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)
biblioteca.adicionar_livro(livro1)

