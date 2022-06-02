def function(n,count):
    for i in range(2,n+1):
        if(n%i==0):
            n=n//i
            op[count]=i
            count=count+1
            function(n,count)
            break
        elif(n%i!=0):
            continue
        elif(n==1):
            break
    return count
def main():
    op={}
    count=0
    n=int(input())
    function(n,count)
    for i in range(0,len(op)):
        if i==len(op)-1:
            print(op[i],end='')
        else:
            print(str(op[i])+'*',end='')
main()
