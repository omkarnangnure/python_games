rule = "Welcome to the game created by Omkar.\nThe rules are\n 1.Guess the no between 1 to 100 only"
import random
i = random.randint(1,101)
n=[]
pt=True
def ip():
    return int(input("Enter the number:"))
while pt:
    p = ip()
    n.append(abs(p-i))
    if abs(p-i)<11:
        print('Warm')
    else:
        print('Cold')
    if p-i!=0:
        while True:
            p = ip()
            if p==i:
                print("Correct guess")
                pt=False
                break;
            elif abs(p-i)<n[-1]:
                print("Warmer")
            else:
                print("Colder")
            n.append(abs(p-i))
    else:
        print("Correct guess")
            
    
