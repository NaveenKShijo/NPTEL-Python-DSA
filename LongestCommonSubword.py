#  My improving code, on the way of working
LCWtable = {}
def LCW(u,v):
    maxLCW = 0
    for r in range(0,len(u)+1):
        LCWtable[(r, len(v)+1)] = 0
    for c in range(0,len(v)+1):
        LCWtable[(len(u)+1, c)] = 0
    for r in range(len(u)-1,0,-1): # Made a change here len(u) --> len(u)-1
        for c in range(len(v)-1,0,-1): #similar change here
            if(u[r-1] == v[c-1]):
                LCWtable[(r,c)] = 1 + LCWtable[(r+1,c+1)]
            else:
                LCWtable[(r,c)] = 0
            if(LCWtable[(r,c)] > maxLCW):
                maxLCW = LCWtable[(r,c)]
    return maxLCW

word1 = input("Enter first string")
word2 = input("Enter second string")
print(LCW(word1,word2))

#  Right code 
# LCWtable = {}

def LCW(u, v):
    maxLCW = 0
    for r in range(0, len(u)+1):
        LCWtable[(r, len(v))] = 0
    for c in range(0, len(v)+1):
        LCWtable[(len(u), c)] = 0
    for r in range(len(u)-1, -1, -1):
        for c in range(len(v)-1, -1, -1):
            if u[r] == v[c]:
                LCWtable[(r, c)] = 1 + LCWtable[(r+1, c+1)]
            else:
                LCWtable[(r, c)] = 0
            if LCWtable[(r, c)] > maxLCW:
                maxLCW = LCWtable[(r, c)]
    return maxLCW

word1 = input("Enter first string: ")
word2 = input("Enter second string: ")
print(LCW(word1, word2))
