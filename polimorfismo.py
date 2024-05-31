import math


class EquiFigura:
    def __init__(self, longitudLados):
        self.__longitudLados = longitudLados

    def getlongitudLados(self):
        return self.__longitudLados

    def setlongitudLados(self, longitudLados):
        self.__longitudLados = longitudLados

    def __str__(self):
        return f'This figure´s side is {self.__longitudLados} long'


class TrianguloEquilatero(EquiFigura):
    def getPerimetro(self):
        return 3 * self.getlongitudLados()

    def getArea(self):
        lado = self.getlongitudLados()
        return (math.sqrt(3) * math.pow(lado, 2)) / 4


class Cuadrado(EquiFigura):
    def getPerimetro(self):
        return 4 * self.getlongitudLados()

    def getArea(self):
        lado = self.getlongitudLados()
        return lado ** 2


def getPerimetroFigura(figura):
    return figura.getPerimetro()


def getAreaFigura(figura):
    return figura.getArea()


te1 = TrianguloEquilatero(3)
cu1 = Cuadrado(4)

print(f'Equiltrl triangle perimeter: {getPerimetroFigura(te1)} cm2')
print(f'Equiltrl triangle area: {getAreaFigura(te1)} cm2')
print("-------")
print(f'Square perimeter: {getPerimetroFigura(cu1)} cm2')
print(f'Square area: {getAreaFigura(cu1)} cm2')
