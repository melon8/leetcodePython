class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        ans = []
        for i, num in enumerate(nums):
            if target - num in d and i != d[target - num]:
                ans = [i, d[target - num]]
                break
            d[num] = i
            
        return ans
                
        