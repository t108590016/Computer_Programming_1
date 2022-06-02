def message():
    l=list()
    OP=list()    
    n=int(input())
    for i in range(0,n):
        l.append(input())
    n=int(input())
    l2=list()    
    for i in range(0,n):
        l2.append(int(input()))
    
    ls=len(str(l2[0]))
    for i in range(0,len(l)):
        s=l[i]
        ss=int(s[:ls:])
        if len(l2)>0:
            while(len(l2)>0):
                if l2[0]>=ss:
                    
                    OP.append(s[ls+1::])
                    break
                else:
                    
                    l2.remove(l2[0])
                    if len(OP)!=0:
                        if OP[-1]!='-':
                            OP.append('-')
        if len(l2)==0 and s[ls::] not in OP:
            OP.append(s[ls+1::])
    if OP[0]=='-':
        OP.remove(OP[0])
    if OP[-1]=='-':
        OP.remove(OP[-1])
    else:
        for i in range(0,len(OP)):
            print(OP[i])
message()
'''
5
1516843860 Alan: hi, Terry
1516843980 Alan: I'm at ChengCheng stationery shop now
1516844040 Alan: what other materials are missing?
1516844160 Terry: yeah, we still lack 50 pastel papers
1516844220 Terry: could you get it back please?
4
1516843920
1516844100
1516844150
1516844340

'''