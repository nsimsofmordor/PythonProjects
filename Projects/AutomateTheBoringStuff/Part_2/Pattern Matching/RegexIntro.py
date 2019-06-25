import re


def linebreak():
    print("\n" + "=" * 30 + "\n")


# Create a regex object with re.compile
# use r'pattern goes here' to pass in a raw string
# '\n' = new line; '\\n' == r'\n' = '\n'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# The search() method searches the string for matches, and will return None if no pattern found
# The group() will return the actual matched text


# mo is a generic var for 'Match objects'
print("--Object Matching--")

mo = phoneNumRegex.search('My number is 203-535-8947.')
print(f'Phone number found: {mo.group()}')
linebreak()

# Review:
# 1.Import the regex module with import re.
# 2.Create a Regex object with the re.compile() function. (Remember to use a raw string.)
# 3.Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
# 4.Call the Match object’s group() method to return a string of the actual matched text.


# Grouping
print("--Grouping--")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-456-3456')
print(mo.group(1))  # will return 415
print(mo.group(2))  # will return 456-3456
print(mo.group(0))  # will return the whole thing
print(mo.group())  # will return the whole thing
print(mo.groups())  # will return a tuple of the the grouos
linebreak()

# Since groups returns a tuple, we can use tuple unpacking like this:
print("--Naming Tuples--")

areaCode, mainNumber = mo.groups()
print(areaCode + " " + mainNumber)
linebreak()

# What if we want parenthesis to be inside the pattern?
print("--Parenthesis in the pattern--")

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')  # the \( and \) will keep the ()
mo_1 = phoneNumRegex.search('My number is (415) 555-4242')
print(mo_1.groups())
linebreak()

# Matching multiple groups with the Pipe
# 'A'|'B' == "a or b, if both then the first one, 'a' "
print("--Piping--")

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())
mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())
linebreak()

# Piping multiple patterns
print("--Piping Multiple--")

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))
linebreak()

# Optional matching with the question mark
# The ? character flags the group that precedes it as an optional part of the pattern.
print("--Optional groups--")

womanRegex = re.compile(r'Bat(wo)?man')
mo4 = womanRegex.search('The adventures of Batman!')
mo5 = womanRegex.search('The Adventures of Batwoman!')
print(mo4.group())
print(mo5.group())
linebreak()

# Looking for numbers with or without the area code
# Tip: think of ? as saying match zero or one of the group preceding the question mark
print("--With or without area code with optional groups--")

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6 = phoneRegex.search("My number is 324-456-4564")
mo7 = phoneRegex.search("My phone is 345-2643")
print(mo6.group() + "\n" + mo7.group())
linebreak()

# Matching zero or More with a Star
# The * (called the star or asterisk) means “match zero or more”
# — the group that precedes the star can occur any number of times in the text.
print("--Matching with *--")

SuperRegex = re.compile(r'Super(wo)*man')
moA = SuperRegex.search("Look, it is Superman!")
print(moA.group())

moB = SuperRegex.search("Look it is Superwoman!")
print(moB.group())

moC = SuperRegex.search("Look it is Superwowowoman!")
print(moC.group())
linebreak()

# Similar to the *, you can use a + to denote "match one or more" -- which is NOT optional

# Matching specific repetitions
# (ha){3} == 'hahaha' == (ha)(ha)(ha)
# Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the curly brackets.
# (Ha){3,5} == ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
# Regular expressions are greedy by default -- and will try to match the longest possible string

print("--Regex greediness--")
greedyHaRegex = re.compile(r'(Ha){3,5}')  # 'Ha' repeated 3 to 5 times
mog = greedyHaRegex.search('HaHaHaHaHa')
print(mog.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')  # <-- Notice the ? mark
mong = nongreedyHaRegex.search('HaHaHaHaHa')
print(mong.group())

# Tip: Note that the question mark can have two meanings
# in regular expressions: declaring a non-greedy match
# or flagging an optional group.

linebreak()

# While search() will return a Match object of the first match
# the findall() method will return the strings of every match
print("--findall()--")

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))  # returns a list
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(phoneNumRegex.findall(
    'Cell: 415-555-9999 Work: 212-555-0000'))  # returns a list of tuples of strings (of each group)

linebreak()

# Char Classes
# \d Any digit 0-9
# \D Any char that is not a numeric digit 0-9
# \w Any letter, numeric digit, or underscore char (think of this as matching "word" chars
# \s Any space, tab, or newline (think of this as matching "space" characters
# \S Any char this is not a space, tab, or newline

print("--Working with shorthand character classes--")
# This will match text that has one or more numeric digits (\d+),
# followed by a whitespace character (\s),
# followed by one or more letter/digit/underscore characters (\w+).

xmasRegex = re.compile(r'\d+\s\w+')
a = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, '
    '2 doves, 1 partridge')
print(a)

linebreak()

print("--Making your own classes--")
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

linebreak()

print("--Caret and Dollar signs--")
# use (^) at the stat of a regex to indicated that a match must occur at the beginning
# use the ($) at the end of a regex to indicate the string must end with the pattern
# or use both to indicate that the entire string must match the regex

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search("Hello world!"))
print(beginsWithHello.search("He said Hello"))  # returns None

endsWithNum = re.compile(r'\d$')
print(endsWithNum.search('Your num is 42'))
print(endsWithNum.search("42 is your number"))

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('2345432'))
print(wholeStringIsNum.search('234do432'))  # returns none
print(wholeStringIsNum.search('234 5432'))  # returns none

linebreak()

print("--The wildcard character--")

# the . (or dot) char in reg expression is called a wildcard
# it will match any character except for a newline

atRegex = re.compile(r'.at') # will only match one char in front of 'at'
print(atRegex.findall("The cat in the hat sat on the flat mat"))

linebreak()

print("--Matching everything with dot-star--")
#  You can use the dot-star (.*) to stand in for that “anything.”
#  Remember that the dot-character means “any single character except the newline,”
#  and the star-character means “zero or more of the preceding character.”
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

linebreak()

print('--dot-star greediness--')
# the dot-star used greedy mode, trying to match as much text as possible
# us the (.*?) to match in a non greedy way

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

linebreak()

print('--Matching newline with the dot character--')
# The dot-star will match everything except a newline.
# By passing re.DOTALL as the second argument to re.compile(),
# you can make the dot character match all characters,
# including the newline character.

noNewlineRegex = re.compile('.*')  # will ONLY match up the the first new line
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())
print('-------')
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())
linebreak()

# To make the regex case-insensitive, pass the re.IGNORECASE or re.I as the second argument to re.compile()

print('--String Substitution with sub() method--')
# sub(arg1=string to replace, arg2=string for regular expression)

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret docs to Agent Bob.'))

# Sometimes you may need to use the matched text as part of the substitution
# In the first arg of sub(), you can type \1, \2, \3,
# and so on to mean "Enter the text of group 1, 2, 3 and so on in the substitution

agentNamesRegex = re.compile(r'Agent (\w)\w*')  # (group the first letters following the words that come after)
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Even know she was a agent'))
print(agentNamesRegex.findall('Agent Alice told Agent Carol that Agent Even know she was a agent'))

linebreak()

print("--Managing Coomplex Regexes--")
# Verbose Mode, makes it easier to understand complex and long regexes
#phoneRegex = re.comile(r'''(
#    (\d{3}|\(\d{3}\))?            # area code ex: 203 or (203) -- non-greedy
#    (\s|-|\.)?                    # separator ex: a ( ), a (-), or a (.) -- non-greedy
#    \d{3}                         # first three digits ex: 333
#    (\s|-|\.)                     # separator
#    \d{4}                         # last four digits ex: 3333
#    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#    )''', re.VERBOSE)

# Since the re.compile() functions takes ony a single value as a second argument,
# to pass in re.IGNORECASE, re.DOTALL, and re.VERBOSE, you can use the pipe (|)
# which in this context is known as a bitwise operator

# Example: someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

