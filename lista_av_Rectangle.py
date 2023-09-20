#Övningar:
#- Skapa 1000 rektanglar med slumpmässiga dimensioner
#- Skapa en funktion som summerar areorna av alla rektanglar

import random
from klassen_Rectangle import Rectangle

rectangle_list = []

for i in range(1000):
    r = Rectangle()
    r.set_length(random.randint(1, 20))
    r.set_width(random.randint(1, 20))
    rectangle_list.append(r)

def calculateTotalArea(rectangles):
    totalArea=0
    for rectangle in rectangle_list:
        totalArea += rectangle.getArea()
    return totalArea

totalArea = calculateTotalArea(rectangle_list)
print(f"Total area is {totalArea}")



