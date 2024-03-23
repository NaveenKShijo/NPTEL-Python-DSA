
#  Sets in Python
colors = {'red','brown','green','red'}
print(len(colors))
empty_set = set() 
lstToSet = set([23,53,63,21])
fruits = set('Bananab')

# Set Operations
odd = {1,3,5,7,9}
prime = {2,3,5,7,11}
setUnion = odd | prime #{1,2,3,5,7,9,11}
setIntersection = odd & prime #{3,5,7}
setdifference = odd - prime #{1,9}
setExculusiveOr = odd ^ prime #{1,2,9,11}


#  STACKS: You can implement a  stack using a list, pushing and popping out the rightmost elemnet
stack = [65,32,80,94,76,12,31]
stack.append(101)
x = stack.pop() #101
y = stack.pop() #31
print(stack) #[65,32,80,94,76,12,31]


# QUEUES: Implemented using a list, popping out at the head and inserting at the beginning
queue = [43,79,21,53]
x = queue.pop()
queue.insert(0,56)
print(queue)
#  QUEUES are effective for navigating through grids and mazes(Breadth First Search)



