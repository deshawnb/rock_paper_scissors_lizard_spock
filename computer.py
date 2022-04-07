import random
from player import Player

class Computer(Player):
    def __init__(self):
        self.name = self.name_choice()
        super().__init__()
    
    def name_choice(self):
        names = ['Bob', 'John', 'Meg', 'Lois', 'Brian', 'Peter', 'Chris', 'Stewie']
        selected_name = random.choice(names)
        print(f'the computers name is {selected_name}')
        return selected_name

    def role_choice(self):
        selected_role = random.choice(self.gestures)
        return selected_role
