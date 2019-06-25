language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == "Java":
        print('Language is Java')

print(20*"-")

user = "admin"
logged_in = True

if user == "admin" and not logged_in:
    print("Good Credits")
else:
    print("Bad Credits")

print(20*"-")

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # is a and b equal in memory?
print(id(a))
print(id(b))

print(20*"-")

c = a
print(c is a)

# Anything empty, none, or zero will result to false


num = 5
while num != False:
    print(num)
    num -= 1