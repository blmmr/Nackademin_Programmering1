import os
import json

with open('dictionaryNotes.json', 'r') as file:
    notes = json.load(file)

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
        if userValue in notes:
            print(notes[userValue])
            input("Tryck enter för att förstätta...")
        else:
            print("Ogiltig kommand!")
            input("Tryck enter för att förstätta...")
    elif userChoice == "a":
        userValue = input("Ange titel: ")
        userKey = input("Ange text: ")
        notes[userValue] = userKey
        with open('dictionaryNotes.json', 'w') as file:
            json.dump(notes, file) 
        os.system("clear")
        printUI()
        input("Tryck enter för att förstätta...")
    elif userChoice == "r":
        userValue = input("Ange titel som du vill radera: ")
        notes.pop(userValue)
        with open('dictionaryNotes.json', 'w') as file:
            json.dump(notes, file) 
        os.system("clear")
        printUI()
        input("Tryck enter för att förstätta...")
    elif userChoice == "e":
        exit()
    else:
        print("Ogiltig kommand!")
        input("Tryck enter för att förstätta...")