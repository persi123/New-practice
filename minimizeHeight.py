def minimizeH(a,k):
    c=[]
    sum=0
    for i in range(0,len(a)):
        if(a[i]<k):
            c.append(a[i]+k)
        else:
            c.append(a[i]-k)
    c.sort()        
    sum=c[len(c)-1]-c[0]        

    print(sum)            


minimizeH([3, 9, 12, 16, 20],3)