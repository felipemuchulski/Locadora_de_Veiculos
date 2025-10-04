from core.categoria import Categoria

class CadCategoria:
    """
    Cadastro de categorias com adicionar_categorias
    Mostrar o tamanho da lista de categorias com listar_tamanho_categorias
    Buscar pelo nome da categoria com buscar_categoria_nome
    Listar categorias disponíveis com categorias_disponíveis
    """
    def __init__(self):
        self.categorias = []
    
    def adicionar_categorias(self, nome, descricao):
        nova_categoria = Categoria(nome, descricao)
        self.categorias.append(nova_categoria)
    
        
    def listar_tamanho_categorias(self):
        counter = 0
        
        if len(self.categorias) != 0:
            while counter <= len(self.categorias):
                counter += 1

            print(f"O tamanho da lista de categorias é {counter}")
            
        else:
            print("Lista de categorias está vazia")
    
    def categorias_disponiveis(self):
        indice = 0
        if len(self.categorias) != 0:
            for categoria in self.categorias:
                print(f"{indice}. {categoria}")
                indice += 1
        else:
            print("Não existe nenhuma categoria disponível")

    def buscar_categoria_nome(self, nome_categoria):
        for categoria in self.categorias:
            if categoria.nome == nome_categoria:
                print("A categoria foi encontrada:")
                return categoria
        print(f"Categoria '{nome_categoria}' não encontrada")
        return None