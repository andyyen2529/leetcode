# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # 1. Hashmap
        # # check whether the two hasp map are equal
        # # iterate through all the keys
        # # O(s+t) O(s+t)
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True

        # 2. doing sortorder nlog(n)?? n^2 ?? but not quite quick the approach 1 is faster
        return sorted(s) == sorted(t)
