import random


class Game:
    def __init__(self, player1, player2, rounds):
        self.__player1 = player1
        self.__player2 = player2
        self.__rounds = rounds

    def playRound(self):
        player1_heal = random.randint(-25, 25)
        player2_heal = random.randint(-25, 25)

        player1_new_energy = self.__player1.boost(player1_heal)
        player2_new_energy = self.__player2.boost(player2_heal)

        return [player1_new_energy, player2_new_energy]

    def winner(self):
        if self.__player1.getEnergy() > self.__player2.getEnergy():
            return self.__player1
        elif self.__player1.getEnergy() < self.__player2.getEnergy():
            return self.__player2
        else:
            return None

    def play(self):
        for i in range(1, self.__rounds + 1):
            print(f"Round {i}: {self.playRound()}")
