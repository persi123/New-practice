def NextPermutation(a):
    idx=-1
    for i in range(len(a),0,-1):
        if(a[i]>a[i-1]):
            idx=i
            break;
    if(idx==-1):
        a[::-1]
    else:
        prev=idx
        for x in range(idx+1,len(a)):
            if(a[x]>a[idx-1] and a[x]<=a[prev]):
                prev=i
        a[idx-1], a[prev] = a[prev], a[idx-1]
                           





NextPermutation([1,2,3])    