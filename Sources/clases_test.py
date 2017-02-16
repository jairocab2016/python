
class Persona:
    def saludo_general(self):
        return "Hola Persona"


class Estudiante(Persona):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return "Mi nombre es %s \n" % self.nombre


e = Estudiante("Jairo", 25)
e1 = Estudiante("Fabian", 25)
e2 = Estudiante("Pablo", 30)

print e.saludo_general()
print e.hola(), e1.hola(), e2.hola()
