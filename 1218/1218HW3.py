def function():
    n=int(input())
    n1=int(input())
    d={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}
    output=list()
    while(n!=0):
        if n%n1==0:
            output.append(0)
        else:
            if n%n1<10:
                output.append(n%n1)
            else:
                output.append(d[n%n1])
        n=int(n/n1)
        #print(output)
    for i in range(len(output)-1,-1,-1):
        print(output[i],end='')
function()