def IntervalMerge(a):
    m=[]
    for i in range(0,len(a)):
        for k in range(i+1,len(a)):
            if(a[i][1]>a[k][0]):
                a[i][1]=a[k][1]           
    print(a)            






IntervalMerge([[1,3],[2,6],[8,10],[15,18]])        