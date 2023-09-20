#Skapa en ny metod i Rectangle-klassen som beräknar omkretsen
#Skapa två nya objekt av klassen
#Skriv ut area och omkrets för alla objekt

class Rectangle:
    length = 0# Attribut
    width = 0# Attribut

    def getArea(self):# Metod
        return self.length * self.width
    
    def getPerimeter(self):
        return self.length * 2 + self.width * 2
    
    def set_length(self, length):
        if length > 0:
            self.length = length
        else:
            print("Felaktig längd.")

    def get_length(self):
        return self.length
    
    def set_width(self, width):
        if width > 0:
            self.width = width
        else:
            print("Felaktigt nummer.")

    def get_width(self):
        return self.width

#Skapa ett objekt

r3 = Rectangle()
r3.length = 66
r3.width = 7
print(r3.length) 
print(r3.width) 
print(r3.getArea()) 
print(r3.getPerimeter())

print (f"-" * 12)

r3.set_length(2)
print(r3.get_length())
print(r3.getArea()) 

 