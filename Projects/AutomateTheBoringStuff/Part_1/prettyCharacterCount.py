import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# count = {character:number}

# loops over each character, counting how often each character appears

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
# will pprint
pprint.pprint(count)

# without pprint
print(count)


# pprint.pprint(someDictValue) is the same as print(pprint.pformat(someDictValue))

