#Skapa en klass Person med attribut för namn, ålder och adress.
#Skapa en metod som returnerar en kort beskrivning av personen.

class Person:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
    
    def printInfo(self):
        print(f"This person's name is {self.name}! They are {self.age} years old and their address is {self.adress}")

person_1=Person("Anna", 22, "Banergatan 15")
person_1.printInfo()

person_2=Person("Lydia", 35, "Katarina Bangata 10")
person_2.printInfo()

person_3=Person("Sara", 35, "Östberga 4")
person_3.printInfo()