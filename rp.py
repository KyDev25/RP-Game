from random import randint

# Create class wich is called Player


class Player:
    def __init__(self, name, hp, potions, max_attack):
        self.name = name
        self.hp = hp
        self.potions = potions
        self.max_attack = max_attack

    # Method to random attack

    def attack(self, target):
        dammages = randint(5, self.max_attack)
        target.hp -= dammages
        print("\n" + str(self.name) + " a attaqué " + str(target.name) + "\n" + str(target.name) +
              " a perdu " + str(dammages) + " HP\n" + "Il ne lui reste plus que " + str(target.   hp) + " HP !")

    # Method to use random potions

    def use_potions(self):
        if self.potions > 0:
            heal = randint(15, 20)
            self.hp += heal
            self.potions -= 1
            print("\nVous avez utilisé une potion !\n" + "La Potion vous a rajouté " + str(heal) + " HP !\n" +
                  "Il ne vous reste plus que " + str(self.potions) + " Potions !\n" + "Vous avez " + str(self.hp) + " HP !")

    # Method to determinate if Player is dead

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False


player = Player("Bob", 50, 3, 10)
enemy = Player("Satan", 70, 0, 15)

# Function to view intro


def intro():
    return int(input("\nQue souhaitez vous faire ?\n" + "1- Attaquer\n" + "2- Utiliser une potion\n" + "Faîtes votre choix : "))


round = 1
# Function wich is the basic of the Game


def game(round):
    while not player.is_dead() and not player.is_dead():
        print("\nRound " + str(round))
        match intro():
            case 1:
                player.attack(enemy)
                enemy.attack(player)
                if player.hp < 0:
                    print(str(enemy.name) + " vous a vainqu !")
                    return True
                elif enemy.hp < 0:
                    print(str(player.name) + " vous avez vainqu " +
                          str(enemy.name) + " !")
                    return True
                else:
                    return True
            case 2:
                if player.potions > 0:
                    player.use_potions()
                    return True
                else:
                    print("Vous n'avez plus de potions. Vous ne pouvez qu'attaquer")
                    player.attack(enemy)
                    enemy.attack(player)
                return True
            case _:
                print("Ce choix n'existe pas !")
                return True


start = True
while start:
    start = game(round)
    round += 1
