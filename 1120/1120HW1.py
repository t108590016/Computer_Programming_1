def SetOperation(s1,s2,operation):
    d1=dict()
    l1=list()
    OPset=dict()
    OP=False
    #.setdefault(key,value)
    if operation=='|':
        l1=list(s1|s2)
        OP=True
    elif operation=='&':
        l1=list(s1&s2)
        OP=True
    elif operation=='-':
        l1=list(s1-s2)
        OP=True
    elif operation=='^':
        l1=list(s1^s2)
        OP=True
    elif operation=='>':
        print(s1>s2)
    elif operation=='<':
        print(s1<s2)
    elif operation=='>=':
        print(s1>=s2)
    elif operation=='<=':
        print(s1<=s2) 
    else:
        print(s1==s2)
    if OP==True:
        for i in range(0,len(l1)):
            d1.setdefault(l1[i],i)
        sOP=sorted(d1)
        for i in range(0,len(sOP)):
            OPset[i]=sOP[i]
        print('{',end='')
        for i in range(0,len(sOP)):
            print("'",end='')
            print(sOP[i],end='')
            print("'",end='')
            if i!=len(sOP)-1:
                print(', ',end='')
        print('}')
def main():            
    n1=int(input())
    s1=input().split(' ')
    operation=input()
    n2=int(input())
    s2=input().split(' ')
    s1=set(s1)
    s2=set(s2)
    SetOperation(s1,s2,operation)

main()