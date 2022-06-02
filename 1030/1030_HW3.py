def function():
    n=input().split(' ')
    ni=list()
    ns=list()
    n1=list()    
    m=list()
    count=0 
    for i in range(0,len(n)):
        ni.append(int(n[i]))
    ni.sort()
    for i in range(0,len(ni)):
        ns.append(str(ni[i]))
    function1(ns,n1,ns,count,m)
    print(minnum)
def function1(n,n1,n2,count,m):
    if(count==0):
        count+=1    
        for i in range(0,len(n2)):
            n1=list()
            n2=n.copy()
            if((i!=len(n2)-1)and(n2[i]!=n2[i+1]))or(i==len(n2)-1):
                n1.append(n2[i])
                n2.remove(n2[i])
                function2(n,n1,n2,count,m)   
def function2(n,n1,n2,count,m):
    count+=1
    if(count<len(n)):  
        for i in range(0,len(n2)):
            n3=n2.copy()
            n4=n1.copy()
            if(((i!=len(n3)-1)and(n3[i]!=n3[i+1]))or(i==len(n3)-1)):
                n4.append(n2[i])
                n3.remove(n2[i])
                function2(n,n4,n3,count,m)
    elif(count==len(n)):
        global minnum
        dl=list()
        s=''
        if n1[-1]!=n2[0]:
            n1.append(n2[0])
            n2.remove(n2[0])
            for i in range(0,len(n1)-1):
                if n1[i]==n1[i+1]:
                    s=''.join(n1)                     
                    dl.append(int(s))
            s=''.join(n1)
            m.append(int(s))
            if(len(dl)>0):
                for i in range(0,len(dl)):
                    if(dl[i] in m):
                        m.remove(dl[i])
            if(len(m)>0):
                minnum=m[0]            
        else:
            del n1,n2                  
function()
