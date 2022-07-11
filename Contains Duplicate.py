# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # method 2. sorting
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: # two adjacent pointers 
                return True
        return False
        
        # # method 3. hashset
        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False