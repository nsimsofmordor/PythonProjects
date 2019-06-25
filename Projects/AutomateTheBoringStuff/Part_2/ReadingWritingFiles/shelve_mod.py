# You can sve variables in your python programs to binary shelf files
# Therefore your program can restore data to variables from the hard drive

import shelve
mydatapath = '/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles/mydata'
shelfFile = shelve.open(mydatapath)
cats = ['Bob','Frank', 'Tony']
shelfFile['cats'] = cats
shelfFile.close()

# will save a file mydata.db

# retrieving the data

shelfFile = shelve.open('/home/nsims/PycharmProjects/PythonProjects/Projects/AutomateTheBoringStuff/Part_2/ReadingWritingFiles/mydata')
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
