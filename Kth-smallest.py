def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    print(arr)
    print(arr[k-1])                     
                
kthSmallest([7 ,10, 4, 3 ,20, 15], 0, 5, 3)