class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [0] * (size)
        prefix = [1] * (size)
        suffix = [1] * (size)

        curr = 1
        for i in range(1, size):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(size - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(size):
            output[i] = prefix[i] * suffix[i]
        
        return output