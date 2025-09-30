from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, valorLocacao, categoria, disponivel, cilindrada):
        super().__init__(placa, marca, modelo, valorLocacao, categoria, disponivel)
        self.cilindrada = cilindrada
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"{self.cilindrada} cilindradas")
    