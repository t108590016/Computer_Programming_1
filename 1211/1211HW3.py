def code():
    l=input().split()
    s=''
    for i in range(0,len(l)):
        s+=l[i]
    code=''
    count=0
    s_set=set()
    for char in s:
        if char.isdigit():
            code+=char
        elif char in s_set:
            continue
        else:
            count=s.count(char)
            if count<10:    
                code+=str(count)
            s_set.add(char)
    #print(s)
    print(code)
    #print(s_set)
code()
'''
Be9tter to light one candle than to curse the darkness xxxxxxxxxxx
'''