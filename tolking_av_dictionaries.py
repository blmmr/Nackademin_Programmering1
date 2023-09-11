person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris","age": 3,"typ": "dog"},
        {"name": "Lisa","age": 3,"typ": "cat"} 
        ]
}

#lösning 1
print(f"{person['firstname']} {person['lastname']} är {person['age']} år gammal och har {len(person['pets'])} husdjur:")
for pet in person['pets']:
    print(f"* En {pet['age']}  år gammal {pet['typ']} som heter {pet['name']}")

#lösning 2
pet_1 = person['pets'][0]
pet_2 = person['pets'][1]

print(f"* En {pet_1['age']} år gammal {pet_1['typ']} som heter {pet_1['name']}")
print(f"* En {pet_2['age']} år gammal {pet_2['typ']} som heter {pet_2['name']}")