def function(s1,s2,l1,l2):
    if l1==0: #如果s1的長度等於0
        return l2 #回傳s2的長度
    if l2==0: #如果s2的長度等於0
        return l1 #回傳s1的長度
    if s1[l1-1]==s2[l2-1]: #如果兩字串的最後一個字一樣
        return function(s1,s2,l1-1,l2-1) #往前一個字繼續比
    return 1+min(function(s1,s2,l1,l2-1),function(s1,s2,l1-1,l2-1),function(s1,s2,l1-1,l2)) 
    #都沒有，計數+1，比較三種情形，找到三個之中最小的
    
    
def main():
    s1=input()
    s2=input()
    print(function(s1,s2,len(s1),len(s2)))
main()
