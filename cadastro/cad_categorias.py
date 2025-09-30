from core.categoria import Categoria

class CadCategoria:
    def __init__(self):
        self.categorias = []
    
    def adicionar_categorias(self, nome, descricao):
        nova_categoria = Categoria(nome, descricao)
        self.categorias.append(nova_categoria)
    
    def listar_categorias(self):
        for categoria in self.categorias:
            print(f"Nome: {categoria.nome}, descrição: {categoria.descricao}")
    
    def buscar_categoria_nome(self, nome_categoria):
        for categoria in self.categorias:
            if categoria.nome == nome_categoria:
                print("A categoria foi encontrada:")
                return categoria
        print(f"Categoria '{nome_categoria}' não encontrada")
        return None