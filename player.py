class Player:
    def __init__(self):
        self.name = self.name_choice()

    def name_choice(self):
        print('Enter a name:')
        user_input = input()
        return user_input

    def role_choice(self):
        print('selct a choice')
        print('1 = rock, 2 = paper, 3 = scissors, 4 = spock, 5 = lizard')
        roll = ''
        while roll == '':
            user_input = input()
            if user_input == '1':
                roll = 'rock'
            elif user_input == '2':
                roll = 'paper'
            elif user_input == '3':
                roll = 'scissors'
            elif user_input == '4':
                roll = 'spock'
            elif user_input == '5':
                roll = 'lizard'
            else:
                print('invalid input')
        print(roll)
        return roll



