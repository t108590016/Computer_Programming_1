def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
def main():
    while(1):
        n=int(input())
        if(n==-1):
            break            
        else:
            print(fibonacci(n))
main()