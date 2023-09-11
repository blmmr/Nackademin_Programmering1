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