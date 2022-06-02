
def check(xHour,yHour,xTime,yTime,xName,yName):
    for i in range(0,xHour):
        for j in range(0,yHour):
            if xTime[i]==yTime[j]:
                    print(str(xName)+' and '+str(yName)+' confict on '+xTime[i])

def conflict():
    ClassName={}
    ClassHour={}
    ClassTimeA={}
    ClassTimeB={}
    ClassTimeC={}
    for i in range(0,3):
        ClassName[i]=input()
        ClassHour[i]=int(input())
        for j in range(0,ClassHour[i]):
            if i==0:
                ClassTimeA[j]=input()
            elif i==1:
                ClassTimeB[j]=input()
            else:
                ClassTimeC[j]=input()
    check(ClassHour[0],ClassHour[1],ClassTimeA,ClassTimeB,ClassName[0],ClassName[1])
    check(ClassHour[1],ClassHour[2],ClassTimeB,ClassTimeC,ClassName[1],ClassName[2])
    check(ClassHour[0],ClassHour[2],ClassTimeA,ClassTimeC,ClassName[0],ClassName[2])          
conflict()

