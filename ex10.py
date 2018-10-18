n=int(input("enter low value: "))
m=int(input("enter high value: "))
for i in range(n,m+1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
