scrores = {'Dhawan':[23,90], 'Sachin':[100,320,12], 'Kohli':[50,80]}
scrores['Sachin'].append(230)
print(scrores['Sachin'])
try:
    scrores['Naveen'].append(560)
except KeyError:
    scrores['Naveen'] = [560]

#  Using get method to access the value of a key in a dictionary
print(scrores.get('Naveen'))

sentence = input("Tell me anything which you want to say \n")
while(True):
    try:
        age = input("Enter your age: \n")
        age = int(age)
    except ValueError:
        print("Enter the age again")
    else:
        break

    

print("The age is :" ,age, "age+1 is " ,age+1)
#  OR 
print(f"The age is : {age} age+1 is {age+1}")

print(sentence)
