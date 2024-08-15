from gerenciamento_mercado.mercado import Mercado
from gerenciamento_mercado.cliente import Cliente
from gerenciamento_mercado.fornecedor import Produto
from gerenciamento_mercado.produto import Fornecedor
from gerenciamento_mercado.transacao import Transacao

# Exemplo de transação no mercado
if __name__ == "__main__":
    mercado = Mercado()

    cliente = Cliente("Carmen Portinho", "123456789", "Rua Pedro Pires, 123")
    mercado.adicionar_cliente(cliente)

    fornecedor = Fornecedor("Fornecedor 1")
    produto = Produto("Arroz", [fornecedor], ["Alimentos"], 25)
    mercado.adicionar_produto(produto)

    transacao = Transacao(produto, cliente, 2)
    mercado.registrar_transacao(transacao)