from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome, espécie="Cachorro")
        self.raça = raça
        
    def fazer_som(self):
        return f"{self.nome} late!"
    
    def buscar(self, objeto):
        return f"{self.nome} está buscando o {objeto}."
    
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, espécie="Gato")
        self.cor = cor
        
    def fazer_som(self):
        return f"{self.nome} mia!"
    
    def arranhar(self, objeto):
        return f"{self.nome} está arranhando o {objeto}."
    
#exemplo de uso
if __name__ == "__main__":      
    cachorro = Cachorro(nome="Rex", raça="Labrador")
    gato = Gato(nome="Mimi", cor="Preto")
    
    print(cachorro.comer())
    print(cachorro.fazer_som())
    print(cachorro.buscar("bola"))
    
    print(gato.dormir())
    print(gato.fazer_som())
    print(gato.arranhar("sofá"))
