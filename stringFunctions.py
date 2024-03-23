# striping the empty spaces in a string
text = "    happy   "
print(text)
print(text.strip())

#  Finding string patterns using Find or Index 
wisdom = "Learn a high Income skill and master Personal Finance"
recepientValue = wisdom.find('Income')
print(recepientValue)

valueRecieved = wisdom.index('Income')
print(valueRecieved)

# Search and Replace
name = "Hai Naveen Hai Naveen Hai Naveen"
newName = name.replace('Naveen', 'Bill Gates')
newName2 = name.replace('Naveen','Elon', 2)
print(newName)
print(newName2)

# Splitting a string
sequence = "1020 : 3040 : 566 : 2341"
columns =sequence.split(" : ")
print(columns)

# Joining Strings
date = "14"
month = "07"
year = "2004"
dob = "-".join([date,month,year])
print(dob)

# Converting case
sentence = "i loVe thIs woRld My maaHn"
print(sentence)
normalSentence = sentence.capitalize()
smallSentence = sentence.lower()
upperSentence = sentence.upper()
titleSentence = sentence.title()
swapSentence = sentence.swapcase()
print(normalSentence,"\n",smallSentence,"\n",upperSentence, "\n", titleSentence, "\n", swapSentence)

# Resizing strings
goal = "Explore"
print(goal.center(50,"*"))
print(goal.center(50,"-"))
print(goal.ljust(30,'$'))
print(goal.rjust(30,'$'))

