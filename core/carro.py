from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, valorLocacao, categoria, disponivel, numeroPortas, automatico):
        super().__init__(placa, marca, modelo, valorLocacao, categoria, disponivel)
        self.numeroPortas = numeroPortas
        self.automatico = automatico
        
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Número de portas: {self.numeroPortas}")
        print(f"Automático: {'Sim' if self.automatico else 'Não'}")