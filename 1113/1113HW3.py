def GCD(n1,n2):
    while(n1!=0 and n2!=0):
        if n1>n2:
            return GCD(n1%n2,n2)
        else:
            return GCD(n2%n1,n1)
    return n1 if n2==0 else n2
def StringGCD(s1,s2):
    s1List=list()
    s2List=list()
    l1=l2=0
    l1=len(s1)
    l2=len(s2)
    #先找出兩個字串長度的最大公因數
    for i in range(0,len(s1),GCD(l1,l2)):
        s1List.append(s1[i:i+GCD(l1,l2)])#把字串切成長度為最大公因數的串列
    for i in range(0,len(s2),GCD(l1,l2)):
        s2List.append(s2[i:i+GCD(l1,l2)])
    gcd=list(set(s1List))
    if(set(s1List)==set(s2List) and len(gcd)==1):#如果裡面的元素完全一樣
        return gcd[0] #回傳元素
    else:
        return 'No GCD' 
def main():
    while(1):
        s=input()        
        if s!='-1':
            ss=s.split(' ')
            s1=ss[0]
            s2=ss[1]
            print(StringGCD(s1,s2))
        else:
            break
main()