class Persona:
    nombre = "jairo"
    edad = 25

    def saludar(self):
        print "Hola %s" % (self.nombre)


objeto = Persona()
objeto.saludar()
