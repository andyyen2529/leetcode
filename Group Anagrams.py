# https://www.youtube.com/watch?v=vzdNOK2oB2E

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # method one sort O(m * nlog n)
        # method two have an hashmap from A to Z O(m*n*26)
        res = defaultdict(list) #{} # mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1 # a = 80, b = 81 ...
            res[tuple(count)].append(s) # 避免count 不存在，可以把dict改成default
        return res.values()
a = Solution()
print(a.groupAnagrams(['aaab', 'aaba','af']))
