direction=[['u',[0,-1]],['d',[0,1]],['l',[-1,0]],['r',[1,0]]] #格式[direction,[x,y]]
n = int(input())
m = int(input())
array=[]
flag=[]
move=[]
for i in range(m):
    array.append([])
    flag.append([])
for i in range(n):
    IP=input().split()
    for j in range(len(IP)):
        array[j].append(int(IP[j]))
        flag[j].append(True)
Answer=False
def getAnswer(col,row,x,y):
    global Answer
    if x == row-1:
        print("".join(move))
        Answer = True
        return 
    for i in direction:
        if col<=y+i[1][1]:
            continue
        if row<=x+i[1][0]:
            continue
        if array[x+i[1][0]][y+i[1][1]] == 0 and flag[x+i[1][0]][y+i[1][1]]:
            flag[x+i[1][0]][y+i[1][1]]=False
            move.append(i[0])
            getAnswer(col,row,x+i[1][0],y+i[1][1])
            move.pop()
            flag[x+i[1][0]][y+i[1][1]]=True
        if Answer == True:
            break
def main():
    getAnswer(n,m,1,0)
    print(n,m,array,flag,move,direction,type(direction))
main()