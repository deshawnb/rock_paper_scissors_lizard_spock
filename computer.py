import random
from player import Player
from gestures import Gestures

class Computer(Gestures):
    def __init__(self):
        super().__init__()
    
    def name_choice(self):
        names = ['Bob', 'John', 'Meg', 'Lois', 'Brian', 'Peter', 'Chris', 'Stewie']
        selected_name = random.choice(names)
        return selected_name

    def role_choice(self):
        selected_role = random.choice(self.gestures)
        return selected_role
