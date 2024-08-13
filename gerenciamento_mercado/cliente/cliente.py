class Cliente():
    def __init__(self):
        pass
    
    def __str__(self):
        return (f'Segue dados do cliente \n'
              f'Nome: {} \n'
              f'Telefone: {} \n'
              f'Endereço: {} \n')


cliente = Cliente('Ana', '99999-999', 'rua fulano sicrano')
print(cliente)
