from datetime import datetime
import math

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, concluida=False, data_conclusao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.set_prioridade(prioridade)
        self.concluida = concluida
        self.data_conclusao = data_conclusao
        
    def set_prioridade(self, prioridade):
        if not 1 <= prioridade <=5:
             raise ValueError("Prioridade deve ser um valor entre 1(baixa) e 5(alta)")
        self.prioridade = prioridade    
        
    def concluir(self):
        self.concluida = True
        self.data_conclusao = datetime.now()

    def __str__(self):
        return (
            f"Tarefa({self.titulo} - {self.descricao}, "
            f"{self.prioridade}, concluida: {self.concluida}, "
            f"data_conclusao: {self.data_conclusao})"
        )

t1 = Tarefa("Estudar", "Revisar POO", 4)
print(t1)

t1.concluir()
print(t1)
t2 = Tarefa("Fazer compras", "Comprar frutas e verduras", 3)
print(t2)
t2.concluir()
print(t2)
