def shortest():
    s1=input()
    s2=input()
    L=list()
    OP=s1
    L1=list()
    for i in range(0,len(s1)):
        for j in range(1,len(s1)+1):
            if(set(s1[i:j])>=set(s2) and len(s1[i:j])>=len(s2)):
                L.append(s1[i:j])
    for i in range(0,len(L)):
        s=list(L[i])
        check=list()
        for j in range(0,len(s2)):
            check.append(False)
        if set(s1)==set(s2):
            for j in range(0,len(s2)):
                if s2[j] in s:
                    s.remove(s2[j])
                if len(s)==0:
                    L1.append(L[i])
        else:
            for j in range(0,len(s2)):
                if s2[j] in s:
                    check[j]=True
                    s.remove(s2[j])
                if set(check)=={True}:
                    L1.append(L[i])
    for i in range(0,len(L1)):
        if(len(L1[i])<len(OP)):
           OP=L1[i] 
    print(OP)
shortest()