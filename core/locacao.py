from veiculo import Veiculo

class Locacao:
    def __init__(self, id, veiculo: Veiculo, dataInicial, dataFinal, valor):
        self.id = id
        self.veiculo = veiculo
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        self.valor = valor
        
    