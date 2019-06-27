class queue:
	def __init__(self):
		self.list=[]
		self.front=0
		self.rear=0
	def push(x):
		self.list.append(x)
		self.rear=self.rear+1
	def pop():
		temp=self.list[self.front]
		self.front=self.front+1
	def display():
		for i in range(self.front,self.rear):
			print(self.list[i])

