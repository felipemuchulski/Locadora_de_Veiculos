from categoria import Categoria
from abc import ABC, abstractmethod

class Veiculo(ABC):
    """
    Classe abstrata Veiculo, que define os principais parâmetros para um novo veículo
    Método abstrado exibir_detalhes para informar as informações do veículo.
    """
    def __init__(self, placa, marca, modelo, valorLocacao, categoria: Categoria, disponivel):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.valorLocacao = valorLocacao
        self.categoria = categoria
        self.disponivel = disponivel
        
    @abstractmethod
    def exibir_detalhes(self):
        ... 