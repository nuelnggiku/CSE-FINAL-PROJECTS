import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Please try again you geuss it wrong')
        elif guess > random_number:
            print('Please try again you guess it too high')

    print(f'Wow you are amazing you have got it {random_number} correctly!!')
    print("I will give you $10.000 Congratulation")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Wow It seems that The computer guessed your number, {guess}, correctly!')


guess(10)