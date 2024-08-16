@property
def quantidade_estoque(self):
        return self._quantidade_estoque
    
@quantidade_estoque.setter
def quantidade_estoque(self, valor):
        if isinstance(valor, (int, float)):
            self._quantidade_estoque = valor
        else:
            raise ValueError("A quantidade de estoque deve ser um número.")

def item_transacionavel(self):#verifica se produto está disponivelpara a venda
        """Verifica se o item está disponível para venda (estoque > 0)."""
        return self.quantidade_estoque > 0

def vender(self, quantidade):#venda do produto
        if not isinstance(quantidade, (int, float)):
            raise ValueError("A quantidade vendida deve ser um número.")
        if quantidade <= 0:
            raise ValueError("A quantidade vendida deve ser positiva.")
        if quantidade > self.quantidade_estoque:
            raise ValueError("Não há estoque suficiente para completar a venda.")
        
        if not self.item_transacionavel():
            raise ValueError("O item não está disponível para venda.")
        
        self.quantidade_estoque -= quantidade
        return f'Venda realizada: {quantidade} unidades de {self.nome_produto} foram vendidas.'

def __str__(self):#retorna uma string
        return (f"Nome: {self.nome_produto}, "
                f"Fornecedores: {', '.join(self.fornecedores)}, "
                f"Categoria: {self.categoria}, "
                f"Quantidade em Estoque: {self.quantidade_estoque}")

# Criando uma instância da classe Produto
produto_arroz = Produto(
    nome_produto='Arroz',
    fornecedores=['Tio João', 'Camil'],
    categoria='Alimentos',
    quantidade_estoque=100
)

# Exibindo informações antes da venda
print(produto_arroz)

# Tentando realizar uma venda
print(produto_arroz.vender(20))

# Exibindo informações após a venda
print(produto_arroz)
