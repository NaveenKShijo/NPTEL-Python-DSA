class Tree:
    """ Each object of this class is a leaf node of a binary search tree """
    def __init__(self, val=None):
        self.value = val
        if(self.value == None):
            self.left = None
            self.right = None
        else:
            self.left = Tree()
            self.right = Tree()
    
    def isEmpty(self):
        return(self.value == None)

    

    
tr1 = Tree(23)
tr2 = Tree()
print(tr1.isEmpty())
print(tr2.isEmpty())
