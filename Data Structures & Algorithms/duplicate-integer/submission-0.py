class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        size = len(nums)
        for i, n in enumerate(nums):
            if i < size - 1 and n == nums[i+1]:
                return True
        return False
        