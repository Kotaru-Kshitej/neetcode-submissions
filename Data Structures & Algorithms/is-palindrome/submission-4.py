class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        b=True
        for i in range(len(s)):
            if not (s[left].isalnum()):
                left+=1
            elif not (s[right].isalnum()):
                right-=1
            elif(s[left].lower()!=s[right].lower()):
                b=False
            else:
                left+=1
                right-=1
        return b

        