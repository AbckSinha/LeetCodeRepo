#Time: O(n)
#Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        # x + y = target
        # target - num in table
        for i, num in enumerate(nums):
            if target - num in table:
                return table[target - num], i
            table[num] = i
        return None
                
        