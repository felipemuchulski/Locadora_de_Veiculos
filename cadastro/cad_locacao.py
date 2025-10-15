from core.locacao import Locacao

class CadLocacao:
    """
    Cadastro de locações com adicionar_locacao
    Mostrar o tamanho da lista de locação com listar_tamanho_locações
    Listar locações disponíveis com locacoes_disponiveis
    Buscar locação pelo indificador retornar_locacao_id
    """
    def __init__(self):
        self.locacoes = []
        
    
    def adicionar_locacao(self, identificador, **kwargs):
        if any(locacao.identificador == identificador for locacao in self.locacoes):
            raise ValueError(f"Já existe este id cadastrado em locações!")
        
        kwargs['identificador'] = identificador

        nova_locacao = Locacao(**kwargs)
        self.locacoes.append(nova_locacao)
    
    def listar_tamanho_locacao(self):
        counter = 0
        if len(self.locacoes) != 0:
            while counter <= len(self.locacoes):
                counter += 1

            print(f"O tamanho da lista de locações é {counter}")
        else:
            print("Você não tem nenhuma locação realizada.")
    
    def locacoes_realizadas(self):
        indice = 0
        if len(self.locacoes) != 0:
            for locacao in self.locacoes:
                print(f"{indice}. {locacao}")
                indice += 1
        else:
            print("Não existe nenhuma locação realizada.")
            
    def retornar_locacao_id(self, id_locacao):
        for locacao in self.locacoes:
            if locacao.identificador == id_locacao:
                print(f"Foi encontrada uma locação com essa identificação {id_locacao}")
                return locacao
            else:
                print("Não existe uma locação com essa informação.")