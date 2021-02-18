
from sys import maxsize
def maxSubarraySum(a):
    max_so_far = -maxsize 
    meh=0
    for x in range(0,len(a)):
       meh=meh+a[x]
       if(meh<a[x]):
           meh=a[x]
       if(max_so_far<meh):
           max_so_far=meh           
    print(max_so_far)

maxSubarraySum([-1,-2,-3,-4])