import random
guesses=0
n=random.randint(0,100)
#guess=input("enter your guess ")
print(n)
while True:
    guess=int(input("enter your guess "))
    if guess==n:
        print("that is the answer")
        print("number of guesses: "+str(guesses))
        break
    else:
        guesses+=1
        if guess<n:
            print("your guess is lower")
        else:
            print("your guess is higher")
       
       
