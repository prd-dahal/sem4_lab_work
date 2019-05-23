
l=[]
w=input("Enter the string")
s=input("Enter a string to see if it's suffix or not")
for i in range(len(w)):
 	l.append(w[i:])
if(s in l):
	if(s==w):
		print("{} is improper suffix of {}".format(s,w))
	else:
		print("{} is proper suffix of {}".format(s,w))
else:
	print("{} is not suffix of {}".format(s,w))
	