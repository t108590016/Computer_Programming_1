def GCD(n1,n2):
    while(n1!=0 and n2!=0):
        if n1>n2:
            return GCD(n1%n2,n2)
        else:
            return GCD(n2%n1,n1)
    return n2 if n1==0 else n1
def main():
    while(1):
        n=input()
        if(n!='-1'):
            ns=list()
            ns=n.split(' ')
            n1=int(ns[0])
            n2=int(ns[1])
            n3=int(ns[2])
            n1n2GCD=GCD(n1,n2)
            print(GCD(n1n2GCD,n3))
        else:
            break
main()