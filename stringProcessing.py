# (i) Searching for text - 1. find(pattern,start,end) : -1, if string is not found
#     2. index(pattern) : ValueError, if string not found

# (ii) Replace - 
# (iii) Splitting -
# (iv) Joining - 
# (v) Converting case
# (vi) Resizing string

text = "Helloo wo)rld"
num = text.find("zebra")
try:
    num2 = text.index("zebra")
except ValueError:
    num2 = "No such words are present in this string"
print (num)
print(num2)

text3 = "THis is Python Python Python Python PythonPython"
newtext3 = text3.replace("Python", "Java")
newtext = text3.replace("Python", "Java", 3)
print(newtext3)
print(newtext)

txtSplit = "This, is Before, splitting"
splitAns = txtSplit.split(', ',1)
print(splitAns)


