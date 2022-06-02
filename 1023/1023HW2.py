def check(N):
    global X
    X=N
    if X=='A':
       X=1
    elif X=='J' or X=='Q' or X=='K':
        X=0.5
    else:
        X=int(X)    
def function():
    global A,B,ScoreA,ScoreB,AnT,BnT
    ip1=input()
    ip1=ip1.split(' ')
    A,B=ip1[0],ip1[1]
    ABang=BBang=False
    ScoreA=ScoreB=0    
    AnT=BnT=An=Bn=1
    check(A)
    A=X
    ScoreA+=X
    check(B)
    B=X
    ScoreB+=X
    while((AnT<5 and BnT<5) and (An!=0 or Bn!=0)):
        ip2=input()
        ip2=ip2.split()
        An=int(ip2[0])
        AnT+=An
        Bn=int(ip2[1+An])   
        BnT+=Bn
        for i in range(0,An):
            A=ip2[i+1]
            check(A)
            A=X
            ScoreA+=X
        for i in range(0,Bn):
            B=ip2[2+An+i]
            check(B)
            B=X
            ScoreB+=X
        if ScoreA>21:
            ABang=True
            ScoreA=0
            break
        elif ScoreB>21:
            BBang=True
            ScoreB=0
            break                
    print('Player','X' if ScoreA>ScoreB else 'Y','is Winner')
    print('Player X $',str(ScoreA) if ABang==False else 'Bang!')
    print('Player Y $',str(ScoreB) if BBang==False else 'Bang!')    
function()