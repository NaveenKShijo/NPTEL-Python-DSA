
class Node:
    def __init__(self, initvalue=None):
        self.value = initvalue
        self.next = None
    def isEmpty(self):
        """ To check whether the given node has empty value"""
        return (self.value == None)
    def append(self, v):
        """ To append new Nodes at the end of a linked list """
        if(self.isEmpty()):
            self.value = v
        elif(self.next == None):
            newNode = Node(v)
            self.next = newNode
        else:
            temp = self.next
            while(True):
                if(temp.next == None):
                    break
                temp = temp.next
            temp.append(v)
    def insert(self, v):
        """To insert a value v at the head of the linked list """
        if(self.isEmpty()):
            self.value = v
        else:
            newInsertNode = Node(v)
            (newInsertNode.value, self.value) = (self.value, v)
            (self.next, newInsertNode.next) = (newInsertNode,  self.next)

    def delete(self, v):
        """ To delete a node carrying a particular value """
        if(self.value == v):
            self.value = self.next.value
            self.next = self.next.next
        else:
            temp = self
            while(True):
                if(temp.next.value == v):
                    break
                else:
                    temp = temp.next
            temp.next = temp.next.next

     
             
n1 = Node(7)
n1.append(32)
n1.append(83)
n1.insert(51)
n1.delete(32)
print("All the values in the linked list are")
i = n1
while(True):
    print(n1.value)
    n1 = n1.next
    if(n1 == None):
        break

