#övning10_3
import pandas as pd
import os

dtype_dict = {"USERID":str, "FORENAME":str, "SURNAME":str, "GENDER":str, "YEAR":str}
df = pd.read_csv("/Users/s/nackademin/programming_1/database.csv", dtype=dtype_dict)

def userUI():
    print(".: PEOPLES DATABASE :.")
    print("----------------------")
    print("get_id | Get person by ID")
    print("scan_f | List people by FORENAME")
    print("scan_s | List people by SURNAME")
    print("scan_g | List people by GENDER")
    print("scan_y | List people by YEAR")
    print("exit   | Exit program")
    print("----------------------")

while True:
    os.system("clear")
    userUI()
    userInput=input("> ")
    if userInput == "get_id": #doesnt work, its empty
        inputId=input("ID > ")
        idNumber_df = df[df["USERID"] == inputId]
        print(idNumber_df)
        input("Press enter to continue > ")
    elif userInput == "scan_f":
        inputName=input("FORENAME > ")
        print(inputName)
        print(type(inputName))
        name_df = df[df["FORENAME"] == inputName]
        print(name_df)
        input("Press enter to continue > ")
    elif userInput == "scan_s":
        inputSurname=input("SURNAME > ")
        surname_df = df[df["SURNAME"] == inputSurname]
        print(surname_df)
        input("Press enter to continue > ")
    elif userInput == "scan_g":
        inputGender=input("GENDER > ")
        gender_df = df[df["GENDER"] == inputGender]
        print(gender_df)
        input("Press enter to continue > ")
    elif userInput == "scan_y":
        inputYear=input("Year > ")
        year_df = df[df["YEAR"] == inputYear]
        print(year_df)
        input("Press enter to continue > ")
    elif userInput == "exit":
        exit()
    else:
        print("Unknown command")
        input("Press enter to continue > ")