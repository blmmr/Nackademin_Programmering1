character = {
'forename': 'Shrek',
'surename': 'orc',
'occupation': 'warrior'
}

for i in character:
    print(i)#print first column

for key in character:
    print (character[key])#print  second column

character["land"] = "sweden" #add an item
del character["land"] #delete an item

print(character["forename"])#skrivs ut Shrek

print(character)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) #creating a dictionary

#hämta en value
print(f"Hej! {character['forename']}")

#nested dictionaries
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[2]['age'])
print(people[1]['sex'])