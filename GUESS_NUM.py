import random
print("WELCOME TO GUESS THE NUMBER GAME")
print("The game is very simple. You just have to guess the number between the range of 1 to 100")
attempts = 0
rd = random.randrange(1,100)
while(True):
    n = int(input('Guess the number:'))
    if n < rd:
        print('Number is smaller')
        attempts += 1
    elif n > rd:
        print('Number is bigger')
        attempts += 1
    elif n == rd:
        print('You guessed it correctly')
        attempts += 1
        print('score:' , attempts)
        break
    
