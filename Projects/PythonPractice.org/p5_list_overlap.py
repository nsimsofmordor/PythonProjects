'''Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  and write a program that returns a list that contains only the
  elements that are common between the lists (without duplicates).
  Make sure your program works on two lists of different sizes.
  Extras:
    Randomly generate two lists to test this
  '''

import random as rand

l_1 = []
l_2 = []
l_common = []

for x in range(25):
    l_1.append(rand.randint(0,26))
for i in range(10):
    l_2.append(rand.randint(0,26))

l_1.sort()
l_2.sort()
print(l_1)
print(l_2)

for x in l_1:
    if x in l_2:
        if x not in l_common:
            l_common.append(x)

l_common.sort()
print(l_common)





