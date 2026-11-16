class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = [0] * 2 

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in seen:
                res = [seen.get(diff), i]
                break
            seen[nums[i]] = i
        return res

            
                


