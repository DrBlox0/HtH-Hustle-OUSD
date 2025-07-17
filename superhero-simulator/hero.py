
import random
from abilities import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armor = []
        self.abilities = []

    def battle(self, opponent):
    # fight another opponenet and randomly choose a winner
        self.opponent = opponent
        winner = random.choice([self, opponent])
        print(f"The winner is: {winner.name}")
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def sum_of_attacks(self):
        total_damage = 0 

        for ability in self.abilities: 
            total_damage += ability.attack()

        return total_damage
    
    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        total_block = 0

        for armor in self.armor:
            total_block += armor.block()

        return total_block

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health) 

    my_hero.battle(my_hero)