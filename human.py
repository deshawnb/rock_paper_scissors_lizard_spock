from player import Player
class Human(Player):
    def __init__(self):
        self.name = self.name_choice()
        super().__init__()