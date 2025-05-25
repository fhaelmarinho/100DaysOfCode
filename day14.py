# ✨ 100 Days of Code Challenge - Day 14/100 💻

class Livro:
    def __init__(self, titulo, autor, ano, genero, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.disponivel = disponivel
    
    def emprestar(self):
        if self.disponivel:            
            print(f"O livro {self.titulo} está disponível")
            self.disponivel = False
        else:
            print(f"O livro {self.titulo} não está disponível para emprestimo")


    def devolver(self):
        if self.disponivel == False:
            print(f"O livro {self.titulo} foi devolvido")
        else:
            print(f"O livro {self.titulo} não foi emprestado")
            self.disponivel = True
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.genero} - {self.ano} "
    
class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []
        
    def emprestar_livro(self, livro):
        if livro.disponivel == True:
            livro.emprestar()
            self.livros_emprestados.append(livro)
        else:
            print(f"O livro {livro.titulo} não está disponível para emprestimo")
            
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
        else:
            print(f"O livro {livro.titulo} não foi emprestado para você")
    
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        return f"Livro: {livro.titulo} adicionado com sucesso."
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return f"Usuário: {usuario.nome} registrado!"
    
    def listar_livros_disponiveis(self):
        for livro in self.livros:
            if livro.disponivel:
                print (f"Disponíveis: {livro}")
                
    def listar_livros_emprestados(self):
        for livro in self.livros:
            if not livro.disponivel:
                print (f"Emprestados: {livro}")


# Criando biblioteca
bib = Biblioteca()

# Criando livros
l1 = Livro("Dom Casmurro", "Machado de Assis", "Literatura Brasileira", 1899)
l2 = Livro("A Moreninha", "Joaquim Manuel de Macedo", "Literatura Brasileira", 1844)

# Adicionando livros
bib.adicionar_livro(l1)
bib.adicionar_livro(l2)

# Criando usuário
u1 = Usuario("Ana", 1)

# Registrando usuário
bib.registrar_usuario(u1)

# Emprestando livro
u1.emprestar_livro(l1)

# Listando livros
bib.listar_livros_disponiveis()
bib.listar_livros_emprestados()
