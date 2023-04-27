import random
while(1):
    print("\t\t\t!!!WELCOME TO THE STRONGEST PASSWORD GENERATOR!!!")
    i = int(input("Press 1 to generate your password || Press 2 to exit : "))
    if i == 2:
        break

    l = ['!','@','$','&']

    ls = ['a1','a2','a3']

    p = ''

    k = random.randint(8,12)
    for i in range(k):
    
        q = random.choice(ls)

        a1 = chr(random.randint(65,122))
        a2 = str(random.randint(1,9))
        a3 = random.choice(l)

        p += eval(q)

    pas1 = p.replace('',' ').split()

    random.shuffle(pas1)

    print("".join(pas1))



