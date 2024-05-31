MAX_ENERGY = 100
MIN_ENERGY = 0

class Player:
    def __init__(self, idPlayer, nickName):
        self.__idPlayer = idPlayer
        self.__nickName = nickName
        self.__energy = (MAX_ENERGY + MIN_ENERGY) // 2


    def getIdPlayer(self):
        return self.__idPlayer
    def getNickName(self):
        return self.__nickName
    def getEnergy(self):
        return self.__energy


    def setIdPlayer(self, idPlayer):
        self.__idPlayer = idPlayer
    def setNickName(self, nickName):
        self.__nickName = nickName
    def __setEnergy(self, energy):
        if MIN_ENERGY <= energy <= MAX_ENERGY:
            self.__energy = energy
        else:
            print(f"Energy must be set between {MIN_ENERGY} and {MAX_ENERGY}.")

    def toString(self):
        return f'[Player ID:{self.__idPlayer}, Player nickname:{self.__nickName}, Player energy:{self.__energy}]'

    def boost(self, charge):
        if not isinstance(charge, int):
            charge = 0

        new_energy = self.__energy + charge
        if new_energy > MAX_ENERGY:
            new_energy = MAX_ENERGY
        elif new_energy < MIN_ENERGY:
            new_energy = MIN_ENERGY

        self.__setEnergy(new_energy)

        return charge, self.__energy