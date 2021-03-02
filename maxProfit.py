def maxProfit(a):
    c=[]
    k=a[0]
    l=0
    max=0
    for x in range(1,len(a)):
        if(k>a[x]):
            k=a[x]
            l=x
            max=k
    print(l,max,"pp")        
    for i in range(l,len(a)):
        if(max<a[i]):
            max=a[i]
    print(max-k)
maxProfit([7,4,5,9,6,2])    


