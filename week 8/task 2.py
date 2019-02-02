class car:
    def __init__(self,colour,manufacturer,model,number_of_doors,hp,km):
        self.colour=colour
        self.manufacturer=manufacturer
        self.model=model
        self.number_of_doors=number_of_doors
        self.hp=hp
        self.km=km
    def change_colour(self,colour):
        self.colour=colour
    def change_doors(self,doors):
        self.number_of_doors=doors
    def change_model(self,model):
        self.model=model
    def print_details(self):
        print("Your dream car details are: ")
        print()
        print("Colour ",self.colour)
        print("Manufacturer ",self.manufacturer)
        print("Model ",self.model)
        print("Number of doors",self.number_of_doors)
        print("HorsePower ",self.hp)
        print("Km ",self.km)
print()
carr=car("Red","Bmw","320d",4,162,300000)
carr.print_details()
print()
col=input("Enter your dream colour ")
carr.change_colour(col)
carr.print_details()
print()
doors=input("Enter your dream number of doors ")
carr.change_doors(doors)
carr.print_details()
print()
model=input("Enter your dream model ")
carr.change_model(model)
carr.print_details()
