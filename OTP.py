import random
print('OTP GENERATOR')
d = int(input('How many digits of OTP?'))
out = random.random()
re = str(out)[-d:]
print(f"Your OTP for {n} is :", re)