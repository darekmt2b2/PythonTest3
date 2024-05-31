from jugador import player, MIN_ENERGY, MAX_ENERGY
from game import *


class Test:
    def test1(self):
        jugador = player(1, 'test')
        if jugador.getEnergy() == 50:
            print("Test1 successful: Energy value is correct")
        else:
            print("Test1 Failed: Check your code again")

    def test2(self):
        jugador = player(1, 'test')
        charge_applied, resulting_energy = jugador.boost(-100)
        if resulting_energy == MIN_ENERGY:
            print(f"Test2 successful: Energy's completely depleted: {jugador.getEnergy()}")
        else:
            print("Test2 Failed: Check your code again.")

    def test3(self):
        jugador = player(1, 'test')
        charge_applied, resulting_energy = jugador.boost(200)
        if resulting_energy == MAX_ENERGY:
            print(f"Test3 successful: Energy's completely filled {jugador.getEnergy()}")
        else:
            print("Test3 Failed: Check your code again")

    def test4(self):
        jugador1 = player(1, 'Jack russell')
        jugador2 = player(2, 'Rusty kelpie')
        jugador1.boost(30)
        jugador2.boost(-10)
        partida = Game(jugador1, jugador2, 1)
        if partida.winner() == jugador1:
            print(f"Test4 Passed: El ganador es el jugador con mayor energía {jugador1.toString()}")
        else:
            print("Test4 Failed: Check your code again")


test = Test()
test.test1()
test.test2()
test.test3()
test.test4()
