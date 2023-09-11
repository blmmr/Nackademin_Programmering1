#från listan till json

import json

random_stuff = [1337, 13.37, "Ååh yä!"]
jasonRandomStuff = json.dumps(random_stuff)

print(jasonRandomStuff)