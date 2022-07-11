from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # the max big O is n cube (n^3)
        # for(i=0...n-1): for(j=i...n-1): for(k=i...j) to calculate sum
        # this is wasting time

        # for(i=0...n-1): for(j=i...n-1): curSum + num[j] O(n^2)

        # you will find that in any situation, if you have
        # a negative prefix, you can just ignore them
        # so what you need to do is calculate the prefix
        # and make sure it is positive
        # O(n) linear time

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub



a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 