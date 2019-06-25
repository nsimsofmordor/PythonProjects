# Lists

courses = ['history', 'math', 'English', 'Spanish']

# print(len(courses))

# print(courses[1].upper())

courses.append('art')  # adds to the end of the list
courses.insert(1, 'trig')  # adds to the given index
# print(courses)

courses_2 = ['liberal arts']

courses.append(courses_2)  # will append the list itself
# print(courses)
courses.remove(courses_2)

courses.extend(courses_2)  # will extend the list with elements of the other list
# print(courses)

pop = courses.pop()
# print(pop)

courses.reverse()
# print(courses)

courses.sort()
# print(courses)

# -------

nums = [0, 7, 4, 3, 5, 6, ]

# print(max(nums))

# sortednums = sorted(nums)
# print(sortednums)

# nums.sort()
# print(nums)

# print(nums.index(7))
# print(8 in nums)

# for n in nums:
# print(n)

# -----

names = ['frank', 'pam', 'joe', 'bob']

names_str = ' - '.join(names)  # creating new string with join
# print(names_str)
new_list = names_str.split(' - ')  # creating new list with split
# print(new_list)

new_list[0] = 'Sam'
# print(new_list)

# -----
tup_1 = ('History', 'Math', 'Physics', 'CompSci')
tup_2 = tup_1

# print(type(tup_1))

# print(tup_1)
# print(tup_2)

# tup_1[0] = 'Frank'
# print(tup_1[1])  # tups == lists but ar immutable

# ---
set_1 = {"History", "Math", "English", "CompSci"}
set_2 = {"Western Civ", "Math", "English", "CompSci"}

# print(type(set_1))
# print("Math" in set_1)
#
# print(set_1.intersection(set_2)) # what are the same?
# print(set_1.union(set_2))  # all elements
# print(set_1.difference(set_2))  # Differences

# ---
empty_list = []  # empty_list = list()

empty_tup = ()  # empty_tup = tuple()

empty_set = {}  # NOT CORRECT, this is a dictionary
# print(type(empty_set))
empty_set = set()
# print(type(empty_set))
