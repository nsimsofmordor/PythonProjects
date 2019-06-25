import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# count = {character:number}

# loops over each character, counting how often each character appears

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# pprint.pprint(someDictValue) == print(pprint.pformat(someDictValue))

