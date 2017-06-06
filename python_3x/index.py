
class Punto:
    def __init__(self, x=0, y=0):
        self.mover(x, y)

    def mover(self, x, y):
        self.x = x
        self.y = y

# punto = Punto(4, 2)
# print(punto.x, punto.y)
# puntob = Punto(4)

punto2 = Punto(6)
print(punto2.x, punto2.y)
