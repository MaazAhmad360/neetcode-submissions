class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        if (len(s) > 12):
            return res
        
        def backtrack(s: str, i: int, dots: int, curIp: str):
            if dots == 4 and i == len(s):
                res.append(curIp[1:])
                return
            
            if dots > 4:
                return
            
            j = i + 1
            count = 3
            while(j <= len(s) and count != 0):
                currS = s[i:j]
                if (len(currS) > 1 and currS[0] == '0'):
                    j += 1
                    count -= 1
                    continue
                elif (int(currS) >= 0 and int(currS) < 256):
                    #curIp = curIp + '.' + currS
                    backtrack(s, j, dots+1, curIp + '.' + currS)
                    count -= 1
                    j += 1
                else:
                    break
                
            return
        
        backtrack(s, 0, 0, '')

        return res