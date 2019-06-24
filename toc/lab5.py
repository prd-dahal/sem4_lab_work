#Write a program to for DFA that accepts the strings {ab,bb} over (a,b)
def q0(x):
    return q1
def q1(x):
    if(x=='a'):
        return q3
    else:
        return q2
def q2(x):
    return q3
def q3(x):
    return q3

x=input("Enter a string to check if it belongs to the DFA::")
t=q0(x[0])
for i in range(1,len(x)):
    t=t(x[i])
    
t=(str(t))
t=(t[10:12])
if(t=='q2'):
    print("String Accepted")
else:
    print("String Rejected")