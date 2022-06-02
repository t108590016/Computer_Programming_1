position=[['1',[0,-1]],['2',[0,1]],['3',[-1,0]],['4',[1,0]]]
n = int(input())
m = int(input())
array,flag,move,t,x1=[],[],[],[],[]
for i in range(m):
    array.append([])
    flag.append([])
for i in range(n):
    IP=input().split()
    for j in range(len(IP)):
        array[j].append(int(IP[j]))
        flag[j].append(True)
def getAnswer(col,row,x,y,t):
    if x == row-1:
        t.append("".join(move))
    for i in position:
        if col<=y+i[1][1] or row<=x+i[1][0]:
            continue
        if array[x+i[1][0]][y+i[1][1]] == 0 and flag[x+i[1][0]][y+i[1][1]]:
            flag[x+i[1][0]][y+i[1][1]]=False
            move.append(i[0])
            getAnswer(col,row,x+i[1][0],y+i[1][1],t)
            move.pop()
            flag[x+i[1][0]][y+i[1][1]]=True
getAnswer(n,m,1,0,t)
for i in t:
    x1.append(len(i))
print(min(x1))