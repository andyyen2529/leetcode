from typing import List 
from collections import defaultdict


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2,3,4,5] how many rotation times to become [3,4,5,1,2]
        # L M R if nums[M] >= nums[L] than we are going to check right
        # else check left
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) //2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res 

        

a = Solution()
print(a.findMin([4,5,1,2,3]))