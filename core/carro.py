from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, valorLocacao, categoria, disponivel, numeroPortas, automatico):
        super().__init__(placa, marca, modelo, valorLocacao, categoria, disponivel)
        self.numeroPortas = numeroPortas
        self.automatico = automatico
        
    def exibir_detalhes(self):
        print(f"Informações da placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Modelo do carro: {self.modelo}")
        print(f"Valor da Locação: {self.valorLocacao}")
        print(f"Categoria: {self.categoria}")
        print(f"Está disponível: {self.disponivel}")
        print(f"Número de portas: {self.numeroPortas}")
        print(f"Automático: {'Sim' if self.automatico else 'Não'}")