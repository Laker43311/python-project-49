import math
import prompt
from random import randint


def brain_gcd():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        x = randint(1, 100)
        y = randint(1, 100)
        print('Question:', x, y)
        answer = prompt.integer('Your answer: ')
        if math.gcd(x, y) == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{math.gcd(x, y)}'.")
            print("Let's try again,", name + '!')
            break
    else:
        print('Congratulations,', name + '!')
