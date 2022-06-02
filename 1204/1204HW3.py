def number():
    s=input()
    L=list()
    L_reverse=list()
    numberString=''
    OP=0
    for char in s:
        check=False
        for j in range(0,10):
            if char==str(j):
                numberString+=char
                check=True
                break
        if check==True:
            continue
        else:
            if len(numberString)>0:
                L.append(numberString)
                numberString=''
    if len(numberString)>0:
        L.append(numberString)
    for i in range(0,len(L)):
        numberString=L[i]
        numberReverse=''
        for j in range(len(numberString)-1,-1,-1):
            numberReverse+=numberString[j]
        L_reverse.append(int(numberReverse))
        OP+=int(numberReverse)
    if len(str(OP))==0:
        OP=0
    #print(L,L_reverse)
    print(OP)
number()