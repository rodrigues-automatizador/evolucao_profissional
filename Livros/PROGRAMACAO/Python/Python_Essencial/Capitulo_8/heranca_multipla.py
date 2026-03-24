class Pessoa:
    
    contador = 0
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        Pessoa.contador += 1
        
    @classmethod
    def contar(cls):
        print(f"Foram criados {cls.contador} objetos da classe {cls.__name__}.")
        
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")
        
        
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}. Estou trabalhando.")
        
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")
        

class Gerente(Pessoa, Funcionario):
    def __init__(self, nome, idade, salario, senha):
        super().__init__(self, nome, idade, salario)
        self.senha = senha
        
    def gerenciar(self):
        print(f"{self.nome} está gerenciando.")
        
pessoa1 = Pessoa("Maria", 30)
funcionario1 = Funcionario("João", 3000)

pessoa1.falar("Bom dia!")
funcionario1.falar("Bom dia!")


pessoas = [Pessoa("Maria", 30),
           Funcionario("João", 2000),
           Pessoa("Pedro", 25)]

for pessoa in pessoas:
    print(pessoa.nome)
    
    pessoa.falar("Bom dia!")