# !Python 3
# Regex Search

# import modules
import os, re

# Get the .txt file
def testFile(fileName):
    try:
        fileName.index('.txt')
    except:
        return False
    return True


# Get the list of all files in the current walk
filesList = []
for folders, subFolders, files in os.walk(os.getcwd()):
    for fileName in files:
        filesList.append(os.path.join(folders, fileName))

# Get the regex pattern from the user
pattern = '\d\d\d-\d\d\d-\d\d\d\d\d'
pattern = input("Please input a pattern: ")
  

print("List of all matching patterns: ")
txtFiles = []
for file in filesList:
    if testFile(file):
        File = open(file, 'r')
        FileContent = File.read()
        numbers = re.findall(pattern, FileContent) # make a list of all matching patterns
        if len(numbers) != 0:
            for number in numbers:
                print(number)