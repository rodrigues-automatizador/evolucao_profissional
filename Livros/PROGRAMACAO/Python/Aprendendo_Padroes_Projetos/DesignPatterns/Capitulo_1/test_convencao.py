class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_person(self,):
        return "<Person (%s, %s)>" % (self.name, self.age)
    
p = Person("John", 32)
print("Tipo do objeto: ", type(p), "Memory Address:", id(p))
print(p.get_person())