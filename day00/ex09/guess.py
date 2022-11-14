from random import randint
from sys import stdin

if __name__ == '__main__' :
    print('''\
\
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
\
''')

    number = randint(1, 99)
    attempts = 0

    while True :
        print("What's your guess between 1 and 99?\n>> ", end='')
        cmd = stdin.readline()
        attempts += 1
        if not cmd or cmd == 'exit' :
            print('Goodbye!')
            break
        elif not cmd.isdigit() :
            print("That's not a number.")
        elif int(cmd) > 99 or int(cmd) < 1 :
            print('number sholde be between 1 and 99 !')
        else :
            if int(cmd) > number :
                print ('Too high!')
            elif int(cmd) < number :
                print('Too low!')
            else:
                if number == 42 :
                    print('The answer to the ultimate question of life, the universe and everything is 42.')
                if attempts == 1:
                    print ('Congratulations! You got it on your first try!')
                else:
                    print("Congratulations, you've got it!", f"You won in {attempts} attempts!" , sep='\n')
                break