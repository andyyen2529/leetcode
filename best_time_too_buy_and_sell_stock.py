from typing import List 
from collections import defaultdict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers question
        # L=Buy R=Sell
        # O(n) O(1) it is a two pointers without brute force
        # because in two pointers all elements visit at most twice O(2n)

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r # l += 1 
            r += 1
        return maxProfit