class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            mid = int((high - low) / 2) + low

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
        
        return -1