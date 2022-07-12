# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=KLlXCFG5TnA

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute force O(n*n)
        # 2. One Pass 先扣掉，然後查看hash map是否有這個東西
        # dict val: index
        # 一開始扣掉，扣完查看hashMap沒有結果，就把該值加回去hashmap
        # Time: O(n) Memory O(n)
        prevMap = {} # val: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
a = Solution()
print(a.twoSum([1,2,3,4], 3))

