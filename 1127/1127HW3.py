n=int(input())
d=dict()
vote_list=list()
vote_set=set()
l=list()
count=list()
for i in range(0,n):    
    d.setdefault(i+1,input())
    count.append(0)
n=int(input())
for i in range(0,n):
    vote_list.append(int(input()))
vote_set=list(set(vote_list))
for i in range(0,len(vote_list)):
    for j in range(0,len(vote_set)):
        if str(vote_list[i])==str(vote_set[j]):
            count[int(vote_list[i])-1]+=1
maximun=0
maxposition=0
for i in range(0,len(count)):
    if count[i]>maximun:
        maximun=count[i]
        maxposition=i+1
print(d[maxposition],count[maxposition-1])
'''
5
PASTA
7-ELEVEN
Seafood restaurant
Dessert shop
Ba Fang Yun Ji Dumpling
5
1
2
3
5
5

'''