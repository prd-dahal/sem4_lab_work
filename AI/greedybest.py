graph={'S':[['A',6],['B',5]],'B':[['G',0],['C',6]],'A':[['G',0],['D',8]],'C':None,'G':None,'D':None}
#print(graph['S'][0][1])
fNode='S'
startNode='S'
nextNode=''
print(startNode)
while(fNode!='G'):
    tempNode=''
    tempLength=100000
    try:
        for i in graph[fNode]:
            if(tempLength>i[1]):
                tempNode=i[0]
                tempLength=i[1]
        print(tempNode+'\n')
        fNode=tempNode
    except:
        pass

    