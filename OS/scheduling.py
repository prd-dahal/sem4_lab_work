def fcfs():
	pid=[]
	enterTime=[]
	burstTime=[]
	while(1):
		temp=input("Enter the PID and enter quit when finished").lower()
		if(temp=="quit"):
			break
		else:
			pid.append(temp)
	
	while(1):
		temp=input("Enter the Entry Time and quit when finished").lower()
		if(temp=='quit'):
			break
		else:
			enterTime.append(temp)
	while(1):
		temp=input("Enter the Burst Time and quit when finished").lower()
		if(temp=='quit'):
			break
		else:
			enterTime.append(temp)
		

	