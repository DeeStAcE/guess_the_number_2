def main():
    print('Think od a number between 0 and 1000. I will guess it in 10 steps max. ->')
    min_ = 0
    max_ = 1000

    guess = int((max_ - min_) / 2) + min_
    print(f'I am guessing: {guess}')

    user_ans = input('Did i guess it?\n').lower()
    while user_ans != 'yes':
        if user_ans == 'too small':
            min_ = guess
            guess = int((max_ - min_) / 2) + min_
            print(f'I am guessing: {guess}')
            user_ans = input('Did i guess it?\n').lower()
        elif user_ans == 'too big':
            max_ = guess
            guess = int((max_ - min_) / 2) + min_
            print(f'I am guessing: {guess}')
            user_ans = input('Did i guess it?\n').lower()
        else:
            print('You are cheating!')
            print(f'I am guessing: {guess}')
            user_ans = input('Did i guess it?\n').lower()
    print('I won!')


if __name__ == '__main__':
    main()
