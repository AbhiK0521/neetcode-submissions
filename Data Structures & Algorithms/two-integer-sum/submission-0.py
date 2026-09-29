class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_table = {}
        output = []
        for i in range(len(nums)):
            if target - nums[i] in sum_table:
                output = [sum_table[target - nums[i]], i]
                break
            sum_table[nums[i]] = i
        
        return output
            
