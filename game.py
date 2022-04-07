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
        print('The rules of the game are as follows:\nThe game is best of three, not counting draws.\nRock beats scissors and lizard\nPaper beats rock and spock\nScissors beats paper and lizard\nLizard beats spock and paper\nSpock beats scissors and rock')
    
    def run_game(self):       
        self.announce_winner(self.gameplay(self.assign_players()))

    def assign_players(self):
        if self.gamemode == '1':
            player_one = Computer()
        elif self.gamemode == '2':
            player_one = Human()
        return player_one

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

    def gameplay(self, player_one):
        player_one = player_one
        player_two = Human()
        player_one_wins = 0
        player_two_wins = 0

        while player_one_wins < 2 and player_two_wins < 2:
            player_one_choice = player_one.role_choice()
            player_two_choice = player_two.role_choice()
            if player_one_choice.lower() == 'rock' and player_two_choice.lower() == 'scissors':
                print(f'{player_one.name} crushes {player_two.name}!')
                player_one_wins += 1
            elif player_one_choice.lower() == 'rock' and player_two_choice.lower() == 'lizard':
                print(f'{player_one.name} crushed {player_two.name}!')
                player_one_wins += 1               
            elif player_one_choice.lower() == 'paper' and player_two_choice.lower() == 'rock':
                print(f'{player_one.name} covered {player_two.name}!')
                player_one_wins += 1              
            elif player_one_choice.lower() == 'paper' and player_two_choice.lower() == 'spock':
                print(f'{player_one.name} disproved {player_two.name}!')
                player_one_wins += 1           
            elif player_one_choice.lower() == 'scissors' and player_two_choice.lower() == 'paper':
                print(f'{player_one.name} cut {player_two.name}!')
                player_one_wins += 1              
            elif player_one_choice.lower() == 'scissors' and player_two_choice.lower() == 'lizard':
                print(f'{player_one.name} decapitated {player_two.name}!')
                player_one_wins += 1            
            elif player_one_choice.lower() == 'lizard' and player_two_choice.lower() == 'spock':
                print(f'{player_one.name} poisoned {player_two.name}!')
                player_one_wins += 1             
            elif player_one_choice.lower() == 'lizard' and player_two_choice.lower() == 'paper':
                print(f'{player_one.name} ate {player_two.name}!')
                player_one_wins += 1             
            elif player_one_choice.lower() == 'spock' and player_two_choice.lower() == 'scissors':
                print(f'{player_one.name} smashed {player_two.name}!')
                player_one_wins += 1            
            elif player_one_choice.lower() == 'spock' and player_two_choice.lower() == 'rock':
                print(f'{player_one.name} vaporized {player_two.name}!')
                player_one_wins += 1              
            elif player_two_choice.lower() == 'rock' and player_one_choice.lower() == 'scissors':
                print(f'{player_two.name} crushes {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == 'rock' and player_one_choice.lower() == 'lizard':
                print(f'{player_two.name} crushed {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == 'paper' and player_one_choice.lower() == 'rock':
                print(f'{player_two.name} covered {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == 'paper' and player_one_choice.lower() == 'spock':
                print(f'{player_two.name} disproved {player_one.name}!')
                player_two_wins += 1             
            elif player_two_choice.lower() == 'scissors' and player_one_choice.lower() == 'paper':
                print(f'{player_two.name} cut {player_one.name}!')
                player_two_wins += 1               
            elif player_two_choice.lower() == 'scissors' and player_one_choice.lower() == 'lizard':
                print(f'{player_two.name} decapitated {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == 'lizard' and player_one_choice.lower() == 'spock':
                print(f'{player_two.name} poisoned {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == 'lizard' and player_one_choice.lower() == 'paper':
                print(f'{player_two.name} ate {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == 'spock' and player_one_choice.lower() == 'scissors':
                print(f'{player_two.name} smashed {player_one.name}!')
                player_two_wins += 1             
            elif player_two_choice.lower() == 'spock' and player_one_choice.lower() == 'rock':
                print(f'{player_two.name} vaporized {player_one.name}!')
                player_two_wins += 1              
            elif player_two_choice.lower() == player_two_choice.lower():
                print("It's a draw!")
            else:
                print('Error')
        if player_two_wins >= 2:
            return player_two.name
        elif player_one_wins >= 2:
            return player_one.name

    def announce_winner(self, player_name):
        print(f'The winner of the best of three rounds is {player_name}!')


