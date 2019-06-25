def hello_func(some_name="Nobody"):
    return f"Hello {some_name}"


print(hello_func())
print(hello_func("Bob"))
print(hello_func(some_name="Frank"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# Args are values (Tuples), kwargs are keys and values (Dictionaries)
student_info("math", "art", name="John", age=22)

grades = [89, 90, 99, 79]
teachers = {"Math": "Prof B", "English": "Prof C"}

print(20*"-")

student_info(grades, teachers)  # doesn't pass in values individually
print("\n")
student_info(*grades, **teachers) # this is better
