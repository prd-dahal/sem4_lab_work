l=[]
w=input("Enter a string::")
s=input("Enter another string to check it its substring or not?::")
for i in range(len(w)):
	for j in range(1,(len(w)+1)):
		
		l.append(w[i:j])
while '' in l:
    l.remove('')
if(s in l):
	if(s==w):
		print(s+' is improper substring of '+ w)
	else:
		print(s+' is proper substring of '+ w)
else:
	print(s+' is not improper substring of '+ w)
