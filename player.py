class Player:
    def __init__(self):
        self.name = self.name_choice()

    def name_choice(self):
        print('Enter a name:')
        user_input = input()
        return user_input

    def role_choice(self):
        print(f'{self.name} selct a choice')
        gesetures = ['rock', 'Paper', 'scissors', 'spock', 'lizard']
        print('1 = rock, 2 = paper, 3 = scissors, 4 = spock, 5 = lizard')
        roll = ''
        while roll == '':
            user_input = input()
            if user_input == '1':
                roll = gesetures[0]
            elif user_input == '2':
                roll = gesetures[1]
            elif user_input == '3':
                roll = gesetures[2]
            elif user_input == '4':
                roll = gesetures[3]
            elif user_input == '5':
                roll = gesetures[4]
            else:
                print('invalid input')
        return roll

    

