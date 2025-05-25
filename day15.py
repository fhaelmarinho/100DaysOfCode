# ✨ 100 Days of Code Challenge - Day 15/100 💻

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_informacoes(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Ano: {self.ano}")
    
    def mover(self):
        print (f"O carro está andando pela estrada")
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    def mover(self):
        print("O carro está andando pela estrada")
        
    def exibir_informacoes(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Ano: {self.ano} - Portas: {self.num_portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
        
    def mover(self):
        print("A moto está acelerando pela pista")
        
    def exibir_informacoes(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Ano: {self.ano} - Cilindradas: {self.cilindradas}")    
        
class Garagem:
    def __init__(self):
        self.veiculos = [] 

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)  

    def mostrar_todos(self):
        for veiculo in self.veiculos:  
            veiculo.exibir_informacoes()
            

#Função main() com interação simples
def main():
    garagem = Garagem()
    
    # Criando e adicionando veículos
    carro1 = Carro("Toyota", "Corolla", 2020, 4)
    carro2 = Carro("Renault", "Duster", 2020, 4)             
    moto1 = Moto("Yamaha", "MT-07", 2021, 689)

    garagem.adicionar_veiculo(carro1)
    garagem.adicionar_veiculo(carro2)
    garagem.adicionar_veiculo(moto1)

    # Mostrando todos os veículos
    garagem.mostrar_todos()

# Ponto de entrada
if __name__ == "__main__":
    main()