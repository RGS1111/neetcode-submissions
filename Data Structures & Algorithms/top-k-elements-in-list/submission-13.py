from collections import Counter
from typing import List 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # Frequency buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        # Traverse buckets backwards starting from highest possible frequency
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
