import os


def lb():
    print('+'*30 + '\n')


print('--os path join function-- \n')

# This is a helpful function if you need to create strings for filenames for any OS
print(os.path.join('usr', 'bin', 'spam'))


# for example, this is how you can join names from a list of filenames to the end of a folder name
myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join ('/home/nsims', filename))

lb()

print('--current working dir-- \n')

# how to get the current working dir and change dir
print(os.getcwd())  # print cwd (will be where this file sits
os.chdir('/home/nsims')  # change dir
print(os.getcwd())  # print new dir

lb()

# Creating new folders
#os.makedirs('/home/nsims/newdir/dir')


print('--absolute and relative paths--')
# calling os.path.abs(path)            -- will return the absolute path of the arg
# calling os.path.isab(path)           -- will return true if the arg is an absolute path
# calling os.path.relpath(path, start) -- will return a string of a relative path from the start path to the path
#                                 ^ the start arg by default is the cwd
print(os.path.abspath('.'))
print(os.path.abspath('PythonProjects'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

lb()

print('--dirname and basename--')
# calling os.path.dirname(path)    --will return a string of everything that comes b4 the last slash
# calling is.path.basename(path)   -- will return a string of everything that comes after the last slash

path = "/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles"
print(os.path.basename(path))  # returns the base -- the last thing in the path
print(os.path.dirname(path))  # returns everything b4 the base

# you can use the os.path.split(path) to return a tuple value of the dirname and basename
print(os.path.split(path))

# or the same thing by placing return values inside of a tuple
print((os.path.dirname(path), os.path.basename(path)))

# the os.path.sep is the separator used in the os for the file path
# we can split on this separator to return a list of each part of the path

print(path.split(os.path.sep))  # expect a blank string at the start of the list for linux

lb()

print('--file sizes and folder contents--')
# calling os.path.getsize(path)  -- will return the size in bytes of the file in the path argument
# calling os.listdir(path)       -- will return a list of filename strings for each file in the path

print(os.path.getsize('/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles/os_and_files.py'))
print(os.listdir('/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/PatternMatching'))

lb()

print('--checking path validity--')
#  calling os.path.exists(path)   -- will return True if the file or folder referred to in the argument exists and will return False if it does not exist
#  calling os.path.isfile(path)   -- will return True if the path argument exists and is a file and will return False otherwise
#  calling os.path.isdir(path)    -- will return True if the path argument exists and is a folder and will return False otherwise

print(os.path.exists('/home/nsims'))  # this can be useful to look for a flash drive
print(os.path.exists('/home/frank'))
print(os.path.isdir('/home/nsims'))
print(os.path.isdir('/home/nsims/cert.txt'))
print(os.path.isfile('/home/nsims/cert.txt'))
print(os.path.isfile('/home/nsims'))

lb()

print('--file reading/writing--')
# just working with plaintext files

# Steps: (1) call open() function to return the file object
#        (2) call the read() / write() method on the file object
#        (3) close the file with close() method on the file object


helloFile = open('/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles/hello.txt')
# READING -- with the open(path), open is set to read by default

helloContent = helloFile.read()
print(helloContent)

path = '/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles/sonnet.txt'
sonnetFile = open(path)
# readlines() returns a list of each line
print(sonnetFile.readlines())

helloFile.close()

# WRITING -- pass w as the second arg to open() opens the file as write mode (and will overwrite)
#         -- pass a to append text to the end of the existing file
#         -- if the file does not exist, write/append will create one
path = '/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles/bacon.txt'
#  Creates the file, and write to it
baconFile = open(path, 'w')
baconFile.write("Hi there!\n")  # the write method does not include a new line
baconFile.close()
# appends to the file
baconFile = open(path, 'a')
baconFile.write('Bacon is nasty')
baconFile.close()
# read the file
baconFile = open(path, 'r')  # the 'r' is optional
content = baconFile.read()
print(content)


