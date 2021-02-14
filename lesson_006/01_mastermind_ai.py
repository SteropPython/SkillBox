import mastermind_engine as me
import random


def ai_number():
    while True:
        ai_number = str(random.randint(1000, 9999))
        if len(set(ai_number)) == len(ai_number):
            break
    return ai_number


def user_answer(answer):
    if answer == 'yes' or answer == 'YES':
        me.target_number()
        game()
    elif answer == 'no' or answer == 'NO':
        print('Goodbye')
    else:
        answer = input('\nPlease type again: \n')
        user_answer(answer)


def start_game():
    action = input('Let start GAME? \n Type YES or NO \n')
    user_answer(action)


def game():
    user_attempts = 0
    while True:
        user_number = ai_number()
        print('Artificial intelligence set the number:', ai_number())
        if user_number.isnumeric():
            if len(user_number) != 4:
                print('Try again, enter your four-digit number:')
                continue
            else:
                checker = me.check_number(user_number)
                print('Bulls:', checker['bulls'], 'Cows:', checker['cows'])
        else:
            print('Try again, enter your four-digit number:')
            continue

        user_attempts += 1

        if me.check_result(checker['bulls']):
            break

    print('You made {} attempts'.format(user_attempts))

    user_start_again = input('Play again? \n Type YES or NO \n')

    user_answer(user_start_again)


start_game()
