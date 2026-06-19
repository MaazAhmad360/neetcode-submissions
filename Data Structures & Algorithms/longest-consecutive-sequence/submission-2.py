class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (not len(nums)):
            return 0
        nums.sort()
        max = 0
        curr = 0
        for i in range(len(nums) - 1):
            if curr > max:
                    max = curr
            if (nums[i + 1] == nums[i]):
                continue
            elif (nums[i] + 1) == nums[i + 1]:
                curr += 1
            else:
                if curr > max:
                    max = curr
                curr = 0
        if curr > max:
            max = curr
        return max + 1