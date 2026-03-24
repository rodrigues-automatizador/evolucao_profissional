class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        
    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo")
        
        self.__raio = valor
        