charSet=[]
for i in range(0,2):
    charSet.append(input("Enter the {} character::".format(i+1)))


string=[]
temp=charSet[0]
iteration=int(input("Enter the no of character for string::"))
for i in range(0,iteration):
    while(temp!=charSet[0] or temp!=charSet[1]):
        temp=input("Enter the element::")
        if(temp==charSet[0] or temp==charSet[1]):
            string.append(temp)
            break
        else:
            print("Doesn't match Please Retry")
value=''.join(string)
print("The required string is '{}'".format(value))
    
