import json
import os

attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']
with open('data.json', 'w') as f:
    f.write(json.dumps(attendants))

#os.remove("/Users/s/nackademin/programming_1/data.json")