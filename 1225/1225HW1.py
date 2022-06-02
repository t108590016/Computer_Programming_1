def path(x,y,N,M,L,score, scorelist):
    score+=L[x][y]    
    if(y==M-1 and x==N-1):
        scorelist.append(score)
        return scorelist
    elif x==N-1 and y!=M-1:
        path(x,y+1,N,M,L,score,scorelist)
    elif x!=N-1 and y==M-1:
        path(x+1,y,N,M,L,score,scorelist)
    else:
        path(x+1,y,N,M,L,score,scorelist)
        path(x,y+1,N,M,L,score,scorelist)
def main():
    N=int(input())
    M=int(input())
    L=list()
    scorelist=list()
    score=0    
    for i in range(N):
        L1=list()
        IP=input().split()
        for j in range(M):
            L1.append(int(IP[j]))
        L.append(L1)
    path(0,0,N,M,L,score,scorelist)
    print(min(scorelist))
main()
