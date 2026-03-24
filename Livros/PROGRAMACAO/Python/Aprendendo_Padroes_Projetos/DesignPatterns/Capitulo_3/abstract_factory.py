from abc import ABC, abstractmethod


# ===== Produtos =====
class VegPizza(ABC):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(ABC):
    @abstractmethod
    def serve(self, veg_pizza: VegPizza):
        pass


# ===== Implementações concretas =====
class DeluxeVegPizza(VegPizza):
    def prepare(self):
        print(f"Preparando {self.__class__.__name__}")


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print(f"Preparando {self.__class__.__name__}")


class ChickenPizza(NonVegPizza):
    def serve(self, veg_pizza: VegPizza):
        print(f"{self.__class__.__name__} é servida com frango sobre {veg_pizza.__class__.__name__}")


class HamPizza(NonVegPizza):
    def serve(self, veg_pizza: VegPizza):
        print(f"{self.__class__.__name__} é servida com presunto sobre {veg_pizza.__class__.__name__}")


# ===== Fábricas =====
class PizzaFactory(ABC):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxeVegPizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


# ===== Cliente =====
class PizzaStore:
    def __init__(self, factories):
        self.factories = factories

    def make_pizzas(self):
        for factory in self.factories:
            veg = factory.create_veg_pizza()
            non_veg = factory.create_non_veg_pizza()

            veg.prepare()
            non_veg.serve(veg)


# ===== Execução =====
if __name__ == "__main__":
    store = PizzaStore([IndianPizzaFactory(), USPizzaFactory()])
    store.make_pizzas()