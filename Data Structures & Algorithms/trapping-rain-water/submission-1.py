class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        if not h:
            return 0
        l=0
        r=n-1
        ml=h[l]
        mr=h[r]
        res=0
        while l<r:
            if(ml<mr):
                l+=1
                ml=max(ml,h[l])
                res+=ml-h[l]
            else:
                r-=1
                mr=max(mr,h[r])
                res+=mr-h[r]
        return(res)

