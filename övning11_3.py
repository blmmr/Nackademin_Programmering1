import json
import os

myList = []

def userUI():
    print(".: intMEMORIZER :.")
    print("------------------")
    for i in myList:
        print(f"* {i}")
    print("------------------")
    print(f"SUMMA: {sum(myList)}")
    print("------------------")
    print("mata i heltal")
    print("0 stängar scriptet")

userUI()
while True:
    os.system("clear")
    userUI()
    userInput = input("> ")
    try:
        userInput = int(userInput)
    except:
        print("FEL: Ogiltigt heltal")
    if userInput != 0:
        if userInput not in myList:
            myList.append(userInput)
    else:
        break

jsonMyList = json.dumps(myList)

with open('övning11_3.json', 'w') as f:
    f.write(jsonMyList)