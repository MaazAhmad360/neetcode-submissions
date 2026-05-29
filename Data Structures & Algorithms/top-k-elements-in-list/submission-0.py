class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq = {}

        for n in nums:
            if n in k_freq:
                k_freq[n] += 1
            else:
                k_freq[n] = 1
        
        k_freq = sorted(k_freq.items(), key=lambda item: item[1], reverse=True)

        return [key for key, value in k_freq[:k]]

