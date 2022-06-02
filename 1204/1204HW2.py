def search():
    n=int(input())
    sList=list()
    sUpperList=list()
    KeywordList=KeywordUpperList=list()
    countList=list()
    for i in range(0,n):
        sList.append(input())
        sList.sort()
    for i in range(0,n):
        sUpperList.append(sList[i].upper())
    KeywordList=input().split(' ')
    for i in range(0,len(KeywordList)):
        KeywordUpperList.append(KeywordList[i].upper())
    for i in range(0,len(sUpperList)):
        count=0
        for j in range(0,len(KeywordUpperList)):
            for w in range(0,len(sUpperList[i])-len(KeywordUpperList[j])+1):
                if sUpperList[i][w:w+len(KeywordUpperList[j])]==KeywordUpperList[j]:
                    count+=1
        countList.append(count)
    for w in range(0,len(sUpperList)):
        for i in range(0,len(KeywordUpperList)):
            while(KeywordUpperList[i] in sUpperList[w]):
                start=sUpperList[w].find(KeywordUpperList[i])
                end=sUpperList[w].find(KeywordUpperList[i])+len(KeywordUpperList[i])
                #print(start,end,KeywordList[i],end='')
                sUpperList[w]=sUpperList[w].replace(sUpperList[w][start:end],' '*(end-start))
                sList[w]=sList[w].replace(sList[w][start:end],sList[w][start:end].upper())
                #print(sUpperList[w])
    countListcopy=countList.copy()
    countListsort=countList.copy()
    countListsort.sort(reverse=True)
    pList=list()
    #print(countListsort)
    i=0
    while(i<len(countListcopy)):
        p=countListcopy.index(countListsort[i])
        countListcopy[p]=-1
        pList.append(p)
        i+=1
        #print(pList)
    for i in range(0,len(pList)):
        print(sList[pList[i]])
search()
'''
5
National Taipei University of Technology, Taipei Tech
National Taiwan University of Science and Technology, Taiwan Tech
Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology
Department of Computer Science and Information Engineering, Taipei Tech
Department of Computer Science and Information Engineering, National Taiwan University
Taipei Tech comPuTer Science engineer
'''