
class Auto:
    name=""
    kind=""
    color=""
    value=100.00
    _numero_serie= "kjadaskdasjdkjasjw" #privado
    def description(self):
        desc = "%s es un %s %s. Vale %.2f" % (self.name, self.kind,self.color, self.value)
        return desc

car1= Auto()
car1.name= "Nombre"
car1.color = "Rojo"
car1.value = 13123123.1231

print car1.description()