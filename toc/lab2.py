w=input("Enter the main string::")
s=input("Enter the string to check if its prefix::")
lisX=[w[:i] for i in range(1,len(w)+1)]
if s in lisX:
    if(w==s):
        print("'{}' is proper perfix".format(w))
    else:
        print("'{}' is  improper prefix of '{}'".format(s,w))
else :
    print("'{}' is not the prefix of '{}'".format(s,w))
    
