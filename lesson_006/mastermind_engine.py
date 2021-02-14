import random

TARGET_NUMBER = None


def target_number():
    global TARGET_NUMBER
    while True:
        get_number = str(random.randint(1000, 9999))
        if len(set(get_number)) == len(get_number):
            TARGET_NUMBER = get_number
            break


def check_number(number):
    target_list = []
    user_list = []
    bull = 0
    cow = 0
    for _ in TARGET_NUMBER:
        target_list.append(int(_))
    for _ in number:
        user_list.append(int(_))
    for i in target_list:
        if user_list.count(i) > 0:
            if target_list.index(i) == user_list.index(i):
                bull += 1
            else:
                cow += 1
    return {'bulls': bull, 'cows': cow}


def check_result(bulls):
    if bulls == 4:
        return True
