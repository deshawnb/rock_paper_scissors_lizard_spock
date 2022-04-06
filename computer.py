import random
class Computer:
    def __init__(self):
        self.name = self.name_choice()
    
    def name_choice(self):
        names = ['Bob', 'John', 'Meg', 'Lois']
        selected_name = random.choice(names)
        return selected_name

    def role_choice(self):
        roles = ['Lizard', 'Paper', 'Rock', 'Scissors', 'Spock']
        selected_role = random.choice(roles)
        return selected_role
