def function():
    S=input().split(' ')#字串
    N=input().split(' ')#順序
    S2=list()#排序後的S
    N2=list()#轉成integer的N    
    P=list()#尋找元素在哪
    OP=''#S2轉成字串
    for i in range(0,len(N)):
        N2.append(int(N[i]))
    N2.sort()
    for i in range(0,len(S)):
        P.append(N.index(str(N2[i])))#尋找N的位置
    for i in range(0,len(S)):
        S2.append(S[P[i]])#根據位置加入S2
    OP=''.join(S2)
    print(OP)
function()