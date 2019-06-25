# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Enter a num: "))
num_list = (x for x in range(1, num+1))
div_list = []

for n in num_list:
    if num % n == 0:
        div_list.append(n)

print(div_list)



