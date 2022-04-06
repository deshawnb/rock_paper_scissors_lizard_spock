from player import Player
from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.welcome_message()
        self.rules()
        self.gamemode = self.pick_gamemode()

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')

    def rules(self):
        print('The rules of the game are as follows:\nRock beats scissors and lizard\nPaper beats rock and spock\nScissors beats paper and lizard\nLizard beats spock and paper\nSpock beats scissors and rock')
    
    def pick_gamemode(self):
        valid_input = 0
        while valid_input == 0:
            selected_gamemode = input('Please enter 1 for singleplayer or 2 for 1v1 multiplayer. ')
            if selected_gamemode == '1':
                print('Loading singleplayer!')
                valid_input += 1
                return selected_gamemode
            elif selected_gamemode == '2':
                print('Loading multiplayer!')
                valid_input += 1
                return selected_gamemode
            else:
                print('Sorry, input not recognized, please try again.')
    def gameplay(self):
        pass
Game()