##cpode to find missing number
class Solution:
    def missingNumber(self,array,N):
        # code here
        for n in array:
            k= n+1 
    
            if k not in array:
                print(k)
    
s1=Solution()
A=[1,2,3,5]
s1.missingNumber(A,5)