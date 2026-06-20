class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []

        for i in range(len(nums) - 2):
            target = -1 * nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                currSum = nums[j] + nums[k]
                if( currSum > target):
                    k -= 1
                elif (currSum < target):
                    j += 1
                else:
                    if ([nums[i], nums[j], nums[k]] not in triplets):
                        triplets.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1
        
        return triplets

