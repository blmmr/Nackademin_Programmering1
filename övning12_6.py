import os

notes = {
"Meddelande från skolan": "Friluftsdag på tisdag",
"Kom ihåg!": "Ta bilen till verkstad",
"Inför tentamen": "Gör alla instuderingsuppgifter",
"one": "two"
}

def printUI():
    print(".: ALWAYSNOTE :.")
    print("-- gold edition --")
    print("******************")
    for i in notes:
        print(i)
    print("------------------")
    print("[v]view note")
    print("[a]dd note")
    print("[r]emove note")
    print("[e]xit program")
    print("------------------")

while True:
    printUI()
    userChoice = input("menu >")
    if userChoice == "v":
        userValue = input("> ")
        print(notes[userValue]) #funkar nte
        print("Tryck enter för att förstätta...")
    elif userChoice == "a":
        userValue = input("Ange titel: ")
        userKey = input("Ange text: ")
        notes[userValue] = userKey
        os.system("clear")
        printUI()
        print("Tryck enter för att förstätta...")
    elif userChoice == "r":
        userValue = input("Ange titel som du vill radera: ")
        notes.pop(userValue)
        os.system("clear")
        printUI()
        print("Tryck enter för att förstätta...")
    elif userChoice == "e":
        exit()
    else:
        print("Ogiltig kommand!")
        print("Tryck enter för att förstätta...")