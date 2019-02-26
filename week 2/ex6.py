name=input("Enter your name ")
age=int(input("Enter your age "))
height=int(input("Enter your height in cm "))
weight=int(input("Enter your weight in kg "))
eyes=input("Enter your eyes colour ")
hair=input("Enter your hair colour ")

print("Hello, "+str(name)+" !")
if age<20:
    print("You are young")
elif age>=20 and age<=60:
    print("You are nither young or old")
else:
    print("You are old")
if height<120:
    print("You are short")
elif age>=120 and age<=180:
    print("You are nither short or tall")
else:
    print("You are tall")
if weight<40:
    print("You are fit")
elif weight>=40 and weight<=100:
    print("You are nither fit or fat")
else:
    print("You are fat")
