import prompt
from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        x = randint(1, 100)
        print('Question:', x)
        answer = prompt.string('Your answer: ')
        if x % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif x % 2 != 0 and answer == 'no':
            print('Correct!')
        elif answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was no.")
            print("Let's try again,", name + '!')
            break
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again,", name + '!')
            break
    else:
        print('Congratulations,', name + '!')
