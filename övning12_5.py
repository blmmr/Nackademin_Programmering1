notes = {
"Meddelande från skolan": "Friluftsdag på tisdag",
"Kom ihåg!": "Ta bilen till verkstad",
"Inför tentamen": "Gör alla instuderingsuppgifter"
}

for i, j in notes.items():
  print(i, " : ", j)

userKey = input("Titel > ")
userValue = input("Text > ")

notes[userKey] = userValue

for i, j in notes.items():
  print(i, " : ", j)
