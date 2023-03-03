import prompt
from random import randint


def brain_calc():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('What is the result of the expression?')
    for i in range(3):
        x = randint(20, 100)
        y = randint(1, 20)
        z = randint(0, 2)
        list = ['+', '-', '*']
        print('Question:', x, list[z], y)
        answer = prompt.integer('Your answer: ')
        if answer == x + y:
            print('Correct!')
        elif answer == x - y:
            print('Correct!')
        elif answer == x * y:
            print('Correct!')
        elif list[z] == '+':
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{x + y}'.")
            print("Let's try again,", name + '!')
            break
        elif list[z] == '-':
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{x - y}'.")
            print("Let's try again,", name + '!')
            break
        elif list[z] == '*':
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{x * y}'.")
            print("Let's try again,", name + '!')
            break
    else:
        print('Congratulations,', name + '!')
