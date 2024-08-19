#Criando a classe Fornecedor
class Fornecedor:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
    
    def __str__(self) -> str:
        return(f'Os dados do fornecedor são: {self.nome}, {self.endereco} e {self.cnpj}')


#fornecedor1 = Fornecedor("Nestlé", "Av. Paulista, 123 - SP", "77.377.074/0001-76")
#print(f'Os dados do fornecedor são: {fornecedor1.nome}, {fornecedor1.endereco} e {fornecedor1.cnpj}')