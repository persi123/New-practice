# class Solution:
#     def  twoSum(self, nums,target):
#         i=0
#         a=[]
#         while i < len(nums):
#             j=i+1
#             while j < len(nums):
#                 if nums[i]+nums[j]==target:
#                     a.append(i)
#                     a.append(j)
#                 j+=1
#             if len(a)>1:
#               break    
#             i+=1    
#         print(a)        
#     #   return a


# p1=Solution()

# p1.twoSum([],16021)

# a=4
# k="7"
# k+=str(4)
# print(int(k)+a)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        temp1=l1
        temp2=l2
        a=[]
        b=[]
        i=0
        j=0
        m=0
        n=len(l1)
        k1=""
        k2=""
        result=0
        
        while i<len(temp1):                       #temp1.next!=None:
            a.append(temp1[i])
            #temp1=temp1.next
            i+=1
            
        a.reverse()
        while j<len(temp2):                                   #temp2.next!=None:
            b.append(temp2[j])
            #temp2=temp2.next
            j+=1
        b.reverse()
        while m<len(a):
            print(m)
            k1+=str(a[m])
            k2+=str(b[m])
            m+=1
        print(k1)
        print(k2)
        result=int(k1)+int(k2)
        self.start=None
        while n>0:
            val=result%10
            result=int(result/10)
            newNode=ListNode(val)
            if self.start == None:
                self.start=newNode
            else:
                temp=self.start
                while temp.next!=None:
                    temp=temp.next
                temp.next=newNode
            n-=1
        temp=self.start
        while temp!=None:
            print(temp.val)
            temp=temp.next     
        return newNode
        

p1=Solution()
print(p1.addTwoNumbers([2,4,3],[5,6,4]))