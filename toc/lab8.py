def q0(x):
	if(x==0):
		return q0,q1
	else:
		return q0
def q1(x):
	if(x==1):
		return q2
	else:
		return None
def q2(x):
	return None

x='10110'
t=(q0(1))
print(list(t))
#t=list(t)

# for i in range(1,len(x)):
# 	temp=[]
# 	for j in t:
# 		temp.append(list(j(i)))
# 	t=temp
# 	print(t)