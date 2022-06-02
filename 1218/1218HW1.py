'''

散牌 -> 撲克牌遊戲把單一張牌命名為單張，沒有任何花色牌型，編號 0。
一對 -> 兩張數字一樣的命名為 Pair，編號 1。
兩對 -> 2 組 Pair 的牌稱為 Two pair，編號 2。
三條 -> 三張一樣數字的稱為 Three of a Kind，編號 3。
順子 -> 數字連續的 5 張牌稱為 Straight，包括 13 ,14, 2, 3, 4 或 12, 13 ,14, 2, 3 等，編號 4。
同花 -> 五張同一花色的牌稱為 Flush，編號 5。
葫蘆 -> Three of a Kind 加一個 Pair 稱為 Full House，編號 6。
四條 -> 四張一樣數字稱為 Four of a Kind，編號 7。
同花順 -> 數字連續的 5 張且花色一樣稱為 Straight Flush，編號 8。

'''
def function():
    L=input().split()
    L1=list()
    L2=list()
    quantity=list()
    conti=True
    #print(L)
    for i in range(0,5):
        if L[i][0:2].isdigit():
            L1.append(int(L[i][0:2:]))            
        else:
            L1.append(int(L[i][0]))
        L2.append(L[i][-1])

    L1.sort()
    for i in range(0,4):
        if((2 in L1)and (14 not in L1) and (3 not in L1)):
            conti=False    
        elif(14 in L1) and (2 not in L1) and (13 not in L1):
            conti=False
        elif(L1[i]!=2 and L1[i]!=14 and L1[i]+1!=L1[i+1]):
            conti=False

        
    if len(set(L2))==1 and  conti==True:
        print(8)
    elif len(set(L1))==2:
        s1=list(set(L1))
        for i in range(0,len(s1)):
            quantity.append(L1.count(s1[i]))
        #print(s1)
        if 4 in quantity:    
            print(7)
        elif 3 in quantity and 2 in quantity:
            print(6)

    elif len(set(L2))==1:
        print(5)
    elif conti==True:
        print(4)
    elif len(set(L1))==3:
        s1=list(set(L1))
        for i in range(0,len(s1)):
            quantity.append(L1.count(s1[i]))
        if 3 in quantity:
            print(3)
        elif quantity.count(2)==2:
            print(2)
    elif len(set(L1))==4:
        print(1)
    else:
        print(0)
    #print(conti)
    #print(L1,L2)
    #print(quantity)
function()