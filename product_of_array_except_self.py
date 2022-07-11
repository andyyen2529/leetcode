from typing import List 
from collections import defaultdict

class Solution:     
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can caluculate the prefix array and postfix array of all indexes
        #          1 2 3 4
        # prefix   1 2 6 24
        # postfix 24 24 12 4
        # when you calculate 2: prefix[i-1] * postfix [i+1]
        # you can store all the nums in the output array to save memory
        # output: 1 1 2 6 --> prefix
        # output: 1*24 1*12 2*4 6*1 <-- postfix
        # O(n) O(1)
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        


a_solution = Solution() 
print(a_solution.productExceptSelf([1,2,3,4]))