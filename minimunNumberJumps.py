def minimumJumps(a):
    k=0
    i=0
    while True:
        if i>=len(a)-1:
            k+=1
            break
        else:   
            i+=a[i]
            print(i)
            k+=1 
                      
    print(k-1)    
minimumJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])

# 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9
# 1, 4 ,3, 2, 6, 7 