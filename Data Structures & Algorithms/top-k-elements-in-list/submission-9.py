from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums).items()
        high = -1
        store = {}
        for num, freq in counted:
            if freq > high:
                store[num] = freq
        sort = dict(sorted(store.items(), key=lambda x:x[1]))
        sort_vals = list(sort)
        return sort_vals[-k:]
        
