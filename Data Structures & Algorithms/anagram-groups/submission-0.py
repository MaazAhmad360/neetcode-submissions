class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang_hash = {}
        sublist = []

        for string in strs:
            key = "".join(sorted(string))
            if key in ang_hash:
                ang_hash[key].append(string)
            else:
                ang_hash[key] = [string]
        
        for key, value in ang_hash.items():
            sublist.append(value)
        return sublist
