def km_to_miles(km):
    miles=km * 0.62137
    return miles

def miles_to_km(miles):
    km = miles * 1.60934 
    return km

userDistance = input("Ange distans > (typ 10 km eller 2 miles) ")

distanceParts =userDistance.split()

if len(distanceParts) != 2:
    print("Du måste ange ett nummer och miles eller km")
else:
    value = float(distanceParts[0])
    unit = distanceParts[1]

    if unit == "km":
        miles = km_to_miles(value)
        print(f"{value} km is equal to {miles} miles.")
    else:
        km = miles_to_km(value)
        print(f"{value} miles is equal to {km} km.")