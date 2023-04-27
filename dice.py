import random
print("\t\tWELCOME TO DICE ROLL")

n = int(input("Enter the number of eyes for the dice:"))
a = int(input("Press 1 to roll the dice:"))
while(1):
    
    if a == 1:
         b,c = random.randint(1,6),random.randint(1,6)
         print(b,c)
         break
    
