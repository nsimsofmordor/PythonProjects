# isPhoneNumber.py
# Say you want to find a phone number in a string
# You know the pattern is: ###-###-####


def isPhoneNuber(text):
    if len(text) != 12:  # is it 12 chars?
        return False
    for i in range(0, 3):  # are the first 3 chars nums?
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # is there a hyphen on the 4th char
        return False
    for i in range(4, 7):  # are the 3 chars after the hyphen a num?
        if not text[i].isdecimal():
            return False
    if text[7] != '-':  # is there a hyphen preceding them?
        return False
    for i in range(8, 12):  # are the last 4 digits a number?
        if not text[i].isdecimal():
            return False
    return True

# Testing a valid number with an invalid one
# cell = '203-535-4864'
# print(f'{cell} is a phone number:')
# print(isPhoneNuber(cell))
# print('Moshi Moshi is a phone number: ')
# print(isPhoneNuber('Moshi Moshi'))


# Use case:
message = 'Call my cell at 415-555-1011 tomorrow, if not try my work number at 313-978-8837'
for i in range(len(message)):
    chunk = message[i:i+12]  # take possible chunks of 12 chars - {[0-12], [1-13], [2-14] ...}
    if isPhoneNuber(chunk):  # if chunk contains a valid number, print
        print(f'Phone number found: {chunk}')
print("Done")
