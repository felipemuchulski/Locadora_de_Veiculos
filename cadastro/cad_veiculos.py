from core.veiculo import Veiculo
from core.caminhao import Caminhao
from core.carro import Carro
from core.moto import Moto

class CadVeiculos:
    def __init__(self):
        self.veiculos = []
        
    def cadastrar_veiculo(self, tipo, placa, **kwargs):
        if any(veiculo.placa == placa for veiculo in self.veiculos):
            raise ValueError(f"Já existe um {tipo} cadastrado com a placa '{placa}'")
        
        kwargs['placa'] = placa # Passa a placa pro construtor
        
        if tipo.lower() == "carro":
            veiculo = Carro(**kwargs)
        elif tipo.lower() == "moto":
            veiculo = Moto(**kwargs)
        elif tipo.lower() == "caminhao":
            veiculo = Caminhao(**kwargs)
        else:
            raise ValueError(f"Tipo de veículo '{tipo}' não reconhecido")
        
        self.veiculos.append(veiculo)
        return f"Criado log para teste{veiculo}"
    
    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print("Exibindo veículos")
            print(veiculo)
    
    def buscar_por_placa(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                print(f"Foi encontrado um veículo com a placa {placa}")
                return veiculo
        
        print("Não existe veículo com essa placa")
        return None
    
                