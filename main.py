import numpy as np
file = open(r"C:\\Users\\hassa\\OneDrive\\Desktop\\AI\\file.txt")
m=int(file.read(1))
n=int(file.read(2))
t=int(file.read(3))
file.readline()
lines=file.readlines()
states=lines[0:m]
for x in range(len(states)):
    states[x]=states[x].replace("\n","")
    states[x]=states[x].replace("\t","")
actions=lines[m+1:m+1+n]
for x in range(len(actions)):
    actions[x]=actions[x].replace('\n','')
    actions[x]=actions[x].replace('\t','')
matrix=lines[m+2+n:m+2+n+m]
for x in range(len(matrix)):
    matrix[x]=matrix[x].replace('\n','')
    matrix[x]=matrix[x].replace('\t','')
testcases=lines[m+n+m+3:m+n+m+t+3]
for x in range(len(testcases)):
    testcases[x]=testcases[x].replace('\n','')
tcase=[]
string=''
for x in range(len(testcases)):
    string=testcases[x].split('\t')
    for i in range(len(string)):
        tcase.append(string[i])
stack1=[]
list2=[]
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        list2=matrix[x].split(' ')
    for z in range(len(list2)):
        stack1.append(int(list2[z]))
matrix=np.reshape(stack1,(m,n))
x=0
y=0
solution= []
explored =[]
for y in range(t):
    explored.clear()
    solution.clear()
    index1=states.index(tcase[x])
    index2=states.index(tcase[x+1])
    a=index1
    b=0
    while True:
        if index1==index2:
            break
        elif matrix[a][b]==index2:
            solution.append(actions[b])
            break
        elif a==matrix[a][b] :
            b=b+1
        elif a in explored:
            b=b+1
        else:
            solution.append(actions[b])
            explored.append(b)
            a=matrix[a][b]
            b=0
    x=x+2
    arrowsolution=str(solution)
    arrowsolution=arrowsolution.replace(',','->')
    arrowsolution = arrowsolution.replace('[','')
    arrowsolution = arrowsolution.replace(']','')
    print(arrowsolution)
file.close()