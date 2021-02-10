def maximin(D,start,end):
    e=0;
    k=2;
    for x in range(start,end):
       if x<1:
            if D[0]<D[1]:
                e=D[1]
            else:
                e=D[0]
       else:
            if e<D[k]:
                e=D[k]
                k+=1
    print("maximum:",e)     
    for x in range(start,end):
        if x<1:
            if D[0]<D[1]:
                e=D[0]
            else:
                e=D[1]
        else:
            if e>D[k]:
                e=D[k]
                k+=1
    print("minimum:",e)                       

maximin([10,2,5,9,8],0,4)