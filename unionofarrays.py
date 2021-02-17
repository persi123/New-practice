def union(a,b):
    p=list(set(a) | set(b))
    return p

print(union([5,6],[1,2,6,5]))    