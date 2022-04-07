import random
from player import Player
class Computer(Player):
    def __init__(self):
        super().__init__()
    
    def name_choice(self):
        names = ['Bob', 'John', 'Meg', 'Lois', 'Brian', 'Peter', 'Chris', 'Stewie']
        selected_name = random.choice(names)
        return selected_name

    def role_choice(self):
        roles = ['Lizard', 'Paper', 'Rock', 'Scissors', 'Spock']
        selected_role = random.choice(roles)
        return selected_role
