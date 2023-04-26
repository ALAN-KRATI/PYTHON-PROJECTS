import random
print('Welcome To The Game Of Stone Paper Scissor')
n = input('Enter your name:')
ls = ['Rock', 'Paper', 'Scissor']
out = random.choice(ls)
c = input(f"{n}, Please Enter your choice:")
if out == 'Rock' and c == 'Scissor':
    print('Computer chose:',out)
    print('Computer Wins')
elif out == 'Paper' and c == 'Rock':
    print('Computer chose:',out)
    print('Computer Wins')
elif out == 'Scissor' and c == 'Paper':
    print('Computer chose:',out)
    print('Computer Wins')
else:
    print('Computer chose:',out)
    print(f"{n} Wins")

