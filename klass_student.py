#Skapa en klass Student med attribut för namn och en lista med
#betygspoäng. Skapa en metod för att beräkna studentens
#genomsnittsbetyg. 

class Student:
    def __init__(self, name, grades):
        self.name=name
        self.grades=[grades[0], grades[1], grades[2]]
    
    def getAverageGrade(self):
        averageGrade=sum(self.grades)/len(self.grades)
        averageGrade = round(averageGrade, 2)
        return averageGrade

s1=Student("Johan", [5, 5, 4])
print(s1.getAverageGrade())

s2=Student("Lorry", [3, 2, 5])
print(s2.getAverageGrade())
