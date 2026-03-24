class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
class Conta:
    def __init__(self, numero, cliente, saldo = 0):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = saldo
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente!")
            
        else:
            self.__saldo -= valor
            
    def transferir(self, valor, conta_destino):
        if valor > self.__saldo:
            print("Saldo insuficiente!")
            
        else:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            
    def mostrar_saldo(self):
        print(f"Saldo conta {self.numero}: {self.__saldo}")
        
    
cliente1 = Cliente("João", "123.456.789-00")
cliente2 = Cliente("Maria", "987.654.321-00")

conta1 = Conta(1001, cliente1, 1000)
conta2 = Conta(1002, cliente2)

conta1.transferir(500, conta2)
conta1.mostrar_saldo()
conta2.mostrar_saldo()