# criando classe
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_informacoes(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
    def eh_maior_de_idade(self):
        return f'É maior de idade? {self.idade >= 18}'

# instanciando objeto            
pessoa = Pessoa('Anderson', 25)

# utilizando metodos
print(pessoa.exibir_informacoes())
print(pessoa.eh_maior_de_idade())