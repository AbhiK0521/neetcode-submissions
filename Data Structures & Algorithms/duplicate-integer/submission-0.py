class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_nums = set()
        for num in nums:
            if num in list_nums:
                return True
            list_nums.add(num);
        return False
