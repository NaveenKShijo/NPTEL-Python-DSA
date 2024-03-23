# read(), readline(), readlines()
# write(), writelines()
# flush(), close() IF 'with' IS USED, THEN NO NEED TO USE THEM.
# Copying a file with readlines() & writelines() 
# strip(), lstrip() & rstrip()


# Opening and reading a file
filePath = r"C:\Users\Naveen shijo\Desktop\Python\investing.txt"
with open(filePath, "r") as newFile:
    newFile_content = newFile.read()
    # read() reads entire file into name as a single string
    
    # readline() is used to read a single line from a line
    line1 = newFile.readline()
    line2 = newFile.readline()
    

    # The readlines()  is used to read all lines from a file and return them as a list of strings
    lines = newFile.readlines()


print(newFile_content)
print(line1)
print(line2)

for line in lines:
    print(line)


# Opening and writing to a file
filePath = r"C:\Users\Naveen shijo\Desktop\Python\dummy.txt"
with open(filePath, "w") as file:
    file.write("Hai I am writing to this file usign Python")
    
    # The writelines() is used to write a sequence of strings to a file. It expects a sequence (such as a list) of strings as its argument
    stringList = ['\nLearn the rules of rich', '\nplay by their rules', '\nwin the game']
    file.writelines(stringList)

# Opening and appending the text
filePath = r"C:\Users\Naveen shijo\Desktop\Python\dummy.txt"
with open(filePath, "a") as exisFile:
    exisFile.write("\nThis is new line after writing with python")
