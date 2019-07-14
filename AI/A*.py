graph={'S':[['A',6,4],['B',5,3]],'B':[['G',0,2],['C',6,3]],'A':[['G',0,3],['D',8,2]],'C':None,'G':None,'D':None}
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
            if(tempLength>i[1]+i[2]):
                tempNode=i[0]
                tempLength=i[1]+i[2]
        print(tempNode+'\n')
        fNode=tempNode
    except:
        pass

    