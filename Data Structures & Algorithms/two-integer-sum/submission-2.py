class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        
        for i, n in enumerate(nums):
            if n not in two_sum:
                two_sum[n] = [(i, target - n)]
            else:
                two_sum[n].append((i, target - n))
        
        index_list = []
        for key, pair_list in two_sum.items():
            if len(pair_list)>1 and pair_list[0][1] == pair_list[1][1]:
                return [pair_list[0][0], pair_list[1][0]]
            
            if pair_list[0][1] in two_sum and pair_list[0][1] != key and key == two_sum[pair_list[0][1]][0][1]:
                return [pair_list[0][0], two_sum[pair_list[0][1]][0][0]]


            