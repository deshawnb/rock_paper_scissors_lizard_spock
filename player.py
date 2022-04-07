from gestures import Gestures

class Player(Gestures):
    def __init__(self):
        self.name = self.name_choice()
        self.gestures = ['rock', 'Paper', 'scissors', 'spock', 'lizard']
        super().__init__()

    def name_choice(self):
        print('Enter a name:')
        user_input = input()
        return user_input

    def role_choice(self):
        print(f'{self.name} selct a choice')
        print('1 = rock, 2 = paper, 3 = scissors, 4 = spock, 5 = lizard')
        roll = ''
        while roll == '':
            user_input = input()
            if user_input == '1':
                roll = self.gestures[0]
            elif user_input == '2':
                roll = self.gestures[1]
            elif user_input == '3':
                roll = self.gestures[2]
            elif user_input == '4':
                roll = self.gestures[3]
            elif user_input == '5':
                roll = self.gestures[4]
            else:
                print('invalid input')
        return roll

    

