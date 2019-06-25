

message = "Hello"

print(message)

print(len(message))

print(message[0:5:2])  # string slicing

print(message.lower())  # string methods

print(message.upper())

print(message.find('e'))

message = message.replace('Hello', "GoodBye")
print(message)

greeting = "Hi"
name = "nick"

message = greeting + ' ' + name
print(message)

# string formatting
message = "{} {}, Welcome!".format(greeting, name)
print(message)

message = f"{greeting} {name}, Welcome to string formatting!"
print(message)

# how to find what methods are available
s = 'string'
print(dir(s))

# help function
print(help(str))

print(help(str.format()))