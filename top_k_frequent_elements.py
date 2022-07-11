class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if we create a hash map 1--> 3 2 --> 2 then ascending order, 
        # it is nlog(n)
        # a better way is to create a max heap and pop() the key k times
        # k(pop times) logn for each time to return the pop value total O= klog(n)
        # the best way is to O(n) and O(n) memory
        # using bucket sort
        # i    0 1 2 3 4 5 6 7 8 9 ... 100
        #      3 2 ...                  1  this type doesnt work
        # i(count) 0  1   2   3 4 5 6 (Max length is the length of you nums list)
        # values     [3] [2] [1]
        #  linear time because the length of the list is fixed to the length of nums list
        # in one extreme condition, all exists one time, O(n) + O(n)
        # O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # O(n)
            for n in freq[i]: # 這種請況的極端也只會是 O(n) + O(n)而非square
                res.append(n)
                if len(res) == k:
                    return res
             
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3], 2))