class Cliente:
    def __init__(self, nome, idade, limite):
        self.nome = nome
        self.idade = idade
        self.__limite = limite
        
    def comprar(self, valor):
        if valor > self.__limite:
            print("Compra não autorizada.")
        
        else:
            print("Compra autorizada.")
        
        
cliente = Cliente("Maria", 30, 1000)
cliente._Cliente__limite = 2000
cliente.comprar(1500)