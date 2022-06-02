def function():
    n=int(input())
    IP=list()
    sortlist=list()
    IPlist=list()
    OP=list()
    for i in range(0,n):
        IP.append(input())
    #--------------排序--------------
    for i in range(0,len(IP)):
        s=IP[i].split(',')
        sortlist.append(int(s[0]))
    sortlist2=sortlist.copy()
    indexlist=list()
    sortlist2.sort()
    for i in range(0,len(sortlist)):
        indexlist.append(sortlist.index(sortlist2[i]))
    for i in range(0,len(indexlist)):
        IPlist.append(IP[indexlist[i]])
    #--------------排序--------------
    #--------------合併--------------
    head=end=0
    s1=IPlist[0].split(',')
    minmun1,maxmun1=int(s1[0]),int(s1[-1])
    head,end=minmun1,maxmun1
    for i in range(0,len(IPlist)-1):
        s2=IPlist[i+1].split(',')
        minmun2,maxmun2=int(s2[0]),int(s2[-1])
        if end>=minmun2:
            if maxmun1<maxmun2:
                end=maxmun2
            minmun1=head
            maxmun1=end
            if i==len(IPlist)-2:#當有交集但i已經數到最後時，將現在的頭尾加到輸出
                OP.append(str(head)+','+str(end))
        elif end<minmun2:
            OP.append(str(head)+','+str(end))
            if i==len(IPlist)-2:#當沒交集且i已數到最後，輸出加上輸入的最後一項
                OP.append(IPlist[-1])
            else:#當沒交集但i還沒到最後時，找到新的頭跟尾
                s1=IPlist[i+1].split(',')
                minmun1,maxmun1=int(s1[0]),int(s1[-1])            
                head,end=minmun1,maxmun1
    #--------------合併--------------
    for i in range(0,len(OP)):
        print(OP[i])
function()