def award():
    money=0
    special=input()
    special2=input()
    firstList=input().split(' ')
    sixthList=input().split(' ')
    n=int(input())
    for i in range(0,n):
        IP=input()
        if IP==special:
            money+=10000000
            #print(10000000)
        elif IP==special2:
            money+=2000000
            #print(2000000)
        else:
            for j in range(0,len(firstList)):
                first=firstList[j]
                if IP==first:
                    money+=200000
                    #print(200000)
                    break
                elif IP[-7::]==first[-7::]:
                    money+=40000
                    #print(40000)
                    break
                elif IP[-6::]==first[-6::]:
                    money+=10000        
                    #print(10000)
                    break
                elif IP[-5::]==first[-5::]:
                    money+=4000
                    #print(4000)
                    break
                elif IP[-4::]==first[-4::]:
                    money+=1000
                    #print(1000)
                    break
                elif IP[-3::]==first[-3::]:
                    money+=200
                    #print(200)
                    break
            for j in range(0,len(sixthList)):
                if IP[-3::]==sixthList[j]:
                    money+=200
                    #print(200)
    print(money)
award()
'''
45698621
19614436
96182420 47464012 62781818
928 899 118
5
45698621
96182420
33364012
12341818
76588928
'''
                