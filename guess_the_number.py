def guess_the_number():
    print('Think od a number between 0 and 1000. I will guess it in 10 steps max. ->')
    min_ = 0
    max_ = 1000
    user_ans = ''

    while user_ans != 'yes':
        guess = int((max_ - min_) / 2) + min_
        print(f'I am guessing: {guess}')
        user_ans = get_an_ans()
        if user_ans == 'too small':
            min_ = guess
        elif user_ans == 'too big':
            max_ = guess
    print('I won!')


def get_an_ans():
    correct_ans = ('too small', 'too big', 'yes')
    while True:
        user_ans = input('Did i guess it?\n').lower()
        if user_ans in correct_ans:
            break
        print('Enter a valid answer (too small, too big or yes)')
    return user_ans


if __name__ == '__main__':
    guess_the_number()
