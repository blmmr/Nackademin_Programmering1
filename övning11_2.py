#från json till listan

import json

my_chars = '["abc", "\u00e5\u00e4\u00f6", "123"]'
my_list = json.loads(my_chars)

for i in my_list:
    print(i)