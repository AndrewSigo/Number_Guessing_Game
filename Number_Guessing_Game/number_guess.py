import random

top_of_range = input('Pick a number greater than 0: ')

# isdigit is asking if top_of_range is an int, will return True or False
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Enter a number larger than 0.')
        quit()
else:
    print('Enter a number.')
    quit()

random_num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number.')
        continue

    if user_guess == random_num:
        print('You got it!')
        break
    
    elif user_guess > random_num:
        print('You were above the number!')
    else:
        print('You were below the number!')

print('You got it in', guesses, 'guesses!')

