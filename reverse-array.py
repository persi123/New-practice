def reverse(A,start,end):
    while start<end:
        A[start], A[end]=A[end],A[start]
        start+=1
        end-=1
    print(A)    


A = [1, 2, 3, 4, 5, 6]
reverse(A,0,5)


def reverse(A,start,end):
    for i in range(start,end):
        if(start<end):
            A[start], A[end]=A[end],A[start]
            start+=1
            end-=1
    print(A)    


A = [1, 2, 3, 4, 5, 6]
reverse(A,0,5)
