from core.veiculo import Veiculo
from core.caminhao import Caminhao
from core.carro import Carro
from core.moto import Moto

class CadVeiculos:
    """
    Cadastro de veículos pelo seu tipo com cadastrar_veiculo
    Mostrar o tamanho da lista de veículos com listar_tamanho_veiculos
    Listar veículos disponíveis com veiculos_disponiveis
    Buscar veículo pela placa buscar_por_placa
    """
    
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
    
    def listar_tamanho_veiculos(self):
        counter = 0
        
        if len(self.veiculos) != 0:
            while counter <= len(self.veiculos):
                counter += 1

            print(f"O tamanho da lista de veiculos é {counter}")
        else:
            print("Não existe nenhum veículo cadastrado.")  
            
    def veiculos_diponiveis(self):
        indice = 0
        if len(self.veiculos) != 0:
            for veiculo in self.veiculos:
                print(f"{indice}. {veiculo}")
                indice += 1
        else:
            print("Não existe nenhum veículo disponível.")
    
    def buscar_por_placa(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                print(f"Foi encontrado um veículo com a placa {placa}")
                return veiculo
        
        print("Não existe veículo com essa placa")
        return None
    
                