##cpode to find missing number
class Solution:
    def missingNumber(self,array,n):
        # code here
        for n in array:
            k= n+1 or n-1
    
            if k not in array:
                return k
    
s1=Solution()
A=[1,2,3,4,5,7]
s1.missingNumber(A,7)