#Skapa en klass Employee med attribut för namn, löneinformation
#och anställningsdatum. Skapa en metod som räknar ut antalet år
#som personen har arbetat på företaget. 

from datetime import datetime
class Employee:
    def __init__(self, name, salary, hire_date):
        self.name = name
        self.salary = salary
        self.hire_date = hire_date
    
    def get_years_work(self):
        current_datetime = datetime.now()
        current_year = current_datetime.year
        years_work=current_year-self.hire_date
        return years_work

e1 = Employee("Linda", "33 000", 2019)
print(f"{e1.name} has been working for {e1.get_years_work()} years")

e2 = Employee("Lora", "22 000", 2018)
print(f"{e2.name} has been working for {e2.get_years_work()} years")

e3 = Employee("Kira", "55 000", 2020)
print(f"{e3.name} has been working for {e3.get_years_work()} years")

