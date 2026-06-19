class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr = 0
        s = s.replace(" ", "").lower()
        s = ''.join(char for char in s if char.isalnum())
        rptr = len(s) - 1

        check = True

        while lptr < rptr:
            if s[lptr] != s[rptr]:
                return False
            lptr += 1
            rptr -= 1
        
        return True