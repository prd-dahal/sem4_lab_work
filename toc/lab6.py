#Write a program for DFA that accepts the strings over (a,b) having even number of a's and b's
def q0(x):
    if(x=='a'):
      return q1
    else:
      return q3
def q1(x):
    if(x=='a'):
        return q0
    else:
        return q2
def q2(x):
    if(x=='a'):
        return q3
    else:
        return q1
def q3(x):
    if(x=='a'):
        return q2
    else:
        return q0

x=input("Enter a string to check if it belongs to the DFA::")
t=q0(x[0])
for i in range(1,len(x)):
    t=t(x[i])
    
t=(str(t))
t=(t[10:12])
if(t=='q0'):
    print("String Accepted")
else:
    print("String Rejected")