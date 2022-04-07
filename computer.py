import random
from gestures import Gestures

class Computer(Gestures):
    def __init__(self):
        self.name = self.name_choice()
        super().__init__()
    
    def name_choice(self):
        names = ['Bob', 'John', 'Meg', 'Lois', 'Brian', 'Peter', 'Chris', 'Stewie']
        selected_name = random.choice(names)
        return selected_name

    def role_choice(self):
        gestures = ['rock', 'Paper', 'scissors', 'spock', 'lizard']
        selected_role = random.choice(gestures)
        return selected_role
