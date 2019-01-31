days=int(input("enter how many nights you are goinf to stay: "))
city=str(input("where do you wannt to go? "))
classf=float(input("which class? "))



def hotel(x):
    hotelPrice=(x-1)*70
    return hotelPrice
def plane_ticket(city,classf):
    planePrice=0
    if city=="New York":
        planePrice=2000
    elif city=="Auckland":
        planePrice=790
    elif city=="Venice":
        planePrice= 154
    elif city=="Glasgow":
        planePrice=65
    planePrice=planePrice*classf
    return planePrice

def rental_car(days):
    carprice=days*30
    carprice-=(days/7)*50
    reminder=days%7
    carprice-=(reminder/3)*30
    return carprice
total=hotel(days)+plane_ticket(city,classf)+rental_car(days)
print(total)