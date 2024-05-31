
from jugador import Player
from game import Game

p1 = Player(1, 'Jack russell')
p2 = Player(2, 'Rusty kelpie')

g1 = Game(p1, p2, 3)

print(f"p1: {p1.toString()}")
print(f"p2: {p2.toString()}")

g1.play()

winner = g1.winner()
if winner:
    print(f"The winner is: {winner.toString()}")
else:
    print("Stalemate.")
