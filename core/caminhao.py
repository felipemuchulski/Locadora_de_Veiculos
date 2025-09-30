from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, valorLocacao, categoria, disponivel, cargaEmTonelada):
        super().__init__(placa, marca, modelo, valorLocacao, categoria, disponivel)
        self.cargaEmTonelada = cargaEmTonelada
        
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Carga em tonelada {self.cargaEmTonelada}")