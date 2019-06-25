# {Key:value} == {Identifier:Data}

student = {'name': 'john', 'age': '27', 'courses': ['Math', 'Science']}

print(f"student = {student}")
print(f"student[name] = {student['name']}")
print(f"student['courses'] = {student['courses']}\n")

# print(student['Phone'])  # throws a KeyError, sine that key doesn't exist
print(student.get('phone', 'Not Found'))

print()

print("setting student[phone] = 555-5555")
student['phone'] = '555-5555'
print(student)

print()

print("results of student.update({'name': 'frank'})")
student.update({'name': 'frank'})
print(student)

print()

print("deleting student['age']")
del student['age']
print(student)

print()

print("printing the name...")
name = student['name']
print(name)


print("\nprinting the len of student")
print(len(student))

print("\nprinting the student keys")
print(student.keys())

print("\nprinting the student values")
print(student.values())

print("\nprinting the student items")
print(student.items())

print('\nprinting the key,value pairs')
for key,value in student.items():
    print (key, value)

