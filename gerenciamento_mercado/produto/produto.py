class Produto:#classe Produto estrutura define tipo de objeto com atributos e métodos.
    def __init__(self, nome_produto, fornecedores, categoria, quantidade_estoque): # __init__ chamado na criação de uma nova instância inicializa os atributos do objeto
        self.nome_produto = nome_produto
        self.fornecedores = fornecedores
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque
    
    @property #define uma propriedade para o atributo 
    def nome_produto(self):
        return self._nome_produto
    
    @nome_produto.setter#defini o metodo para definir o valor da propriedade
    def nome_produto(self, valor):
        if isinstance(valor, str):
            self._nome_produto = valor
        else:
            raise ValueError("O nome deve ser uma string.")
  
    @property
    def fornecedores(self):
        return self._fornecedores
    
    @fornecedores.setter
    def fornecedores(self, valor):
        if isinstance(valor, list):
            self._fornecedores = valor
        else:
            raise ValueError("Os fornecedores devem ser uma lista.")
         
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        if isinstance(valor, str):
            self._categoria = valor
        else:
            raise ValueError("A categoria deve ser uma string.")