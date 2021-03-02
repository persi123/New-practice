def Duplicates(a):
    x=0
    for i in range(0,len(a)):
        for k in range(i+1,len(a)):
            if (a[i]==a[k]):
                x=a[i]
    print(x)            








Duplicates([1,1,2])