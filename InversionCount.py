def InversionCount(a):
    c=[]
    for x in range(0,len(a)):
        for j in range(x+1,len(a)):
            if(a[x]>a[j]):
                c.append([a[x],a[j]])
    if(len(c)<1):
        print(0)
    else:
        print(c)            

InversionCount([2, 3, 4, 5, 6])                



