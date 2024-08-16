class Cliente():
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return (f'Segue dados do cliente \n'
              f'Nome: {self.nome} \n'
              f'Telefone: {self.telefone} \n'
              f'Endereço: {self.endereco} \n')


cliente = Cliente('Ana', '99999-999', 'rua fulano sicrano')
print(cliente)
