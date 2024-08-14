class Mercado:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.transacoes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def registrar_transacao(self, transacao):
        transacao.concluir()
        self.transacoes.append(transacao)