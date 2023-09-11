notes = {
"Meddelande från skolan": "Friluftsdag på tisdag",
"Kom ihåg!": "Ta bilen till verkstad",
"Inför tentamen": "Gör alla instuderingsuppgifter"
}

#12.1

title = input("Anteckning > ")
print(notes[title])

#12.2

print("ANTECKNINGAR")
for i in notes:
    print(f"- {i}")

