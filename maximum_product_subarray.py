from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force O(n^2)
        # Better performance
        # positive numbers always makes bigger products
        # negative need to get even numbers
        # 你需要同時記憶每個點的最大與最小值，
        # 因為負最小後面有機會變成正最大(當成上負數)
        # 遇到0先設為1
        res = max(nums) #0 -> [1]
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)  # [-1, -8] 只會想要 -8
            res = max(res, curMax)
        return res



a = Solution()
print(a.maxProduct([2,3,-2,4])) 