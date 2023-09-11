import os

notes = {
"Meddelande från skolan": "Friluftsdag på tisdag",
"Kom ihåg!": "Ta bilen till verkstad",
"Inför tentamen": "Gör alla instuderingsuppgifter"
}

for i, j in notes.items():
  print(i, " : ", j)

print("Lägg till artikel")
userKey = input(print("Titel: "))
userValue = input(print("Text: "))

notes[userKey] = userValue
os.system("clear")

for i, j in notes.items():
  print(i, " : ", j)