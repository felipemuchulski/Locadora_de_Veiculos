from core.locacao import Locacao

class CadLocacao:
    def __init__(self):
        self.locacoes = []
        
    
    def inserir_locacao(self, id, **kwargs):
        if any(locacao.id == id for locacao in self.locacoes):
            raise ValueError(f"Já existe este id cadastrado em locações!")
        
        kwargs['id'] = id
        
        nova_locacao = Locacao(**kwargs)
        self.locacoes.append(nova_locacao)