nums = [x for x in range(6)]

for num in nums:
    if num ==3:
        print("Found")
        break
    print(num)

print(20* "-")

for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)

print(20*"-")

for num in nums:
    for letter in 'xyz':
        print(num, letter)

for i in range(1, 11):
    print(i)

x = 0

while x < 10:
    print(x)
    x += 1
