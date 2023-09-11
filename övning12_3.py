import pprint #pretty print

notes = {
"Meddelande från skolan": "Friluftsdag på tisdag",
"Kom ihåg!": "Ta bilen till verkstad",
"Inför tentamen": "Gör alla instuderingsuppgifter"
}

#3 sätt  att skriva ut dictionary
pprint.pprint(notes, width=1)

print("*************")
print(notes)
print("*************")

for i, j in notes.items():
  print(i, " : ", j)
