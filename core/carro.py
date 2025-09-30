from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, valorLocacao, categoria, disponivel, numeroPortas, automatico):
        super().__init__(placa, marca, modelo, valorLocacao, categoria, disponivel)
        self.numeroPortas = numeroPortas
        self.automatico = automatico
        
    def exibir_detalhes(self):
        detalhes_veiculo = super().exibir_detalhes()
        detalhes_carro = f"Número de portas: {self.numeroPortas}\nAutomático: {'Sim' if self.automatico else 'Não'}"
        return f"{detalhes_veiculo}\{detalhes_carro}"
    