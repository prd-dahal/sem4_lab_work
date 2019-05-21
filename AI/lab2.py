#  ''' write a program to implement production rules to sort system "caabcb" using following production rule
#  	i) ba->ab
#  	ii)ca->ac
#  	iii)cb->bc 
# '''
notInrule=['ba','ca','cb']
def func1(x):
	l=[]
	text=[]
	for i in range(0,len(x),2):
		l.append(x[i:i+2])
	for i in range(len(l)):
		if(l[i] in notInrule):
			text.append(l[i][::-1])
		else:
			text.append(l[i])
	return(''.join(text))
def func2(x):
	l=[x[0]]
	text=[]
	for i in range(1,len(x),2):
		l.append(x[i:i+2])
	
	for i in range(len(l)):
		if(l[i] in notInrule and len(l[i])==2):
			text.append(l[i][::-1])
		else:
			text.append(l[i])
	return (''.join(text))

a='caabcb'
while(notInrule[0] in a or notInrule[1] in a or notInrule[2] in a):
	a=func1(a)
	a=func2(a)


print(a)


