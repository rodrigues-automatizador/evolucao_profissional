class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"{self.nome} foi criado.")
        
    def __del__(self):
        print(f"{self.nome} foi destruído.")
        
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")
        
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem} Estou trabalhando")
        
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")  