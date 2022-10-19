import random

target_num, guess_num = random.randint(1,20 ), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 15 until you get it right : '))
print('You have got $10.000')
print("Congratulation")