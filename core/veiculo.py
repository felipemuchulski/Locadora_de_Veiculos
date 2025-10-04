from categoria import Categoria
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, marca, modelo, valorLocacao, categoria: Categoria, disponivel):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.valorLocacao = valorLocacao
        self.categoria = categoria
        self.disponivel = disponivel
        
    @abstractmethod
    def exibir_detalhes(self):
        ... # Métodos abstratos são somente declarados