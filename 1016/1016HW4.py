def function(n1,n2,s):
    NOcommonfactor=True
    if n1>n2:
        n=n1
    else:
        n=n2
    for i in range(2,n):
        if(n1%i==0 and n2%i==0):
            NOcommonfactor=False
            n1=n1//i
            n2=n2//i
            s=s*i
            function(n1,n2,s)
            break
        else:
            continue
        print(s)
    if NOcommonfactor==True:
        s=s*n1*n2
        print(s)
def main():
    n1=int(input())
    n2=int(input())
    s=1
    if n1==n2:
        s=s*n1
        print(s)
    else:
        function(n1,n2,s)
main()