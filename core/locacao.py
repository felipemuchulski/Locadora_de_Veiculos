from veiculo import Veiculo

class Locacao:
    def __init__(self, identificador, veiculo: Veiculo, dataInicial, dataFinal, valor):
        self.id = identificador
        self.veiculo = veiculo
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        self.valor = valor
        
    