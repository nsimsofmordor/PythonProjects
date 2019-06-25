# def spam(divideBy):
#     return 42 / divideBy
#
# print(spam(2))
# print(spam(12))
# print(spam(0))  # will raise a "ZeroDivisionError"

# try: put code with potential errors here
# except: program moves here if error is activated


def spam(divideby):  # try/except inside function
    try:
        return 42 / divideby  # will try this
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")  # if same error is thrown, execute this code


print(spam(10))
print(spam(20))
print(spam(0))

print(40 * "-")


def spam2(divideby_1):  # try/except outside function
    return 30 / divideby_1


try:
    print(spam2(33))
    print(spam2(22))
    print(spam2(0))
except ZeroDivisionError:
    print("Invalid!")
