class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            target_diff = target - num
            if target_diff in seen:
                return [seen[target_diff], index]
            if num not in seen:
                seen[num] = index
            
        
        
            
        