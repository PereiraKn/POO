class Carro:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def kilometragem(self, km):
        print(f"O carro apresenta {km} quilômetros rodados.")
            
carro = Carro("Chevrolet", "Tracker", 2020)
carro.informacoes()
carro.kilometragem(35000)
